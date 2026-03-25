"""
SureTrip v3 — FastAPI Backend
Multi-city reliability-aware journey planning
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'database'))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import uvicorn

from database import engine, Base, SessionLocal
from models import City, Location, TransportMode
from simulation_engine import DelayPropagationSimulator, LegConfig
from risk_analysis import RiskAnalyzer

import seed_data

CITIES = seed_data.CITIES
ROUTES = seed_data.ROUTES
TRANSPORT_MODES = seed_data.TRANSPORT_MODES

from fastapi import FastAPI
from database import Base, engine
import models

app = FastAPI(title="SureTrip v3 API", version="3.0.0")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Database created"}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root(): return {"message": "SureTrip v3 API", "version": "3.0.0"}

@app.get("/cities")
def get_cities():
    return [{"key": k, "name": v["name"], "lat": v["lat"], "lon": v["lon"],
             "code": v["code"], "emoji": v["emoji"]} for k, v in CITIES.items()]

@app.get("/routes")
def get_routes():
    return [{"src": s, "dst": d, "distance_km": ROUTES[(s,d)]["distance_km"]}
            for s, d in ROUTES.keys()]

@app.post("/plan-journey")
def plan_journey(
    source: str,
    destination: str,
    departure_time: str,
    deadline_time: str,
    n_simulations: Optional[int] = 1000,
):
    src, dst = source.lower().strip(), destination.lower().strip()
    if src not in CITIES or dst not in CITIES:
        raise HTTPException(400, f"Unknown city. Valid: {list(CITIES.keys())}")
    if src == dst:
        raise HTTPException(400, "Source and destination must differ.")

    try:
        dep = datetime.fromisoformat(departure_time)
        dead = datetime.fromisoformat(deadline_time)
    except ValueError:
        raise HTTPException(400, "Invalid datetime format. Use ISO 8601.")

    if dead <= dep:
        raise HTTPException(400, "Deadline must be after departure.")

    route = seed_data.get_route(src, dst)
    n_sims = min(max(n_simulations or 1000, 500), 2000)
    sim_engine = DelayPropagationSimulator(n_simulations=n_sims, random_seed=42)
    analyzer = RiskAnalyzer()
    options_out = []

    for opt_key in ["fastest", "cheapest", "reliable"]:
        if opt_key not in route:
            continue
        tmpl = route[opt_key]
        legs = []
        for i, leg in enumerate(tmpl["legs"]):
            from_hub = seed_data.resolve_location(leg["from"])
            to_hub = seed_data.resolve_location(leg["to"])
            legs.append(LegConfig(
                leg_id=i,
                mode=leg["mode"],
                from_location=from_hub["name"],
                to_location=to_hub["name"],
                base_travel_time=leg["base_time"],
                variance_minutes=leg["variance"],
                buffer_after=leg["buffer"],
                cost=leg["cost"],
                lat_from=from_hub["lat"],
                lon_from=from_hub["lon"],
                lat_to=to_hub["lat"],
                lon_to=to_hub["lon"],
            ))

        sim = sim_engine.simulate(legs, dep, dead)
        total_cost = sum(l.cost for l in legs)
        total_time = sum(l.base_travel_time + l.buffer_after for l in legs) - legs[-1].buffer_after
        risk = analyzer.analyze(legs, sim, tmpl["name"], total_cost, total_time)

        def fmt_arr(minutes):
            from datetime import timedelta
            t = dep + timedelta(minutes=minutes)
            return t.strftime("%H:%M, %d %b")

        options_out.append({
            "type": tmpl["name"],
            "icon": tmpl["icon"],
            "description": tmpl["description"],
            "legs": [
                {
                    "leg_number": i + 1,
                    "mode": l.mode,
                    "mode_display": TRANSPORT_MODES.get(l.mode, {}).get("name", l.mode),
                    "mode_icon": TRANSPORT_MODES.get(l.mode, {}).get("icon", "🚗"),
                    "mode_color": TRANSPORT_MODES.get(l.mode, {}).get("color", "#888"),
                    "from_location": l.from_location,
                    "to_location": l.to_location,
                    "base_travel_time": l.base_travel_time,
                    "variance_minutes": l.variance_minutes,
                    "buffer_after": l.buffer_after,
                    "cost": l.cost,
                    "lat_from": l.lat_from, "lon_from": l.lon_from,
                    "lat_to": l.lat_to, "lon_to": l.lon_to,
                    "avg_delay": round(sim.leg_delay_means[i], 1),
                    "overflow_rate_pct": round(sim.leg_overflow_rates[i], 1),
                }
                for i, l in enumerate(legs)
            ],
            "total_base_time_min": round(total_time, 1),
            "total_cost": total_cost,
            "distance_km": route["distance_km"],
            "probability_of_success": sim.probability_of_success,
            "probability_of_failure": sim.probability_of_failure,
            "risk_level": risk.risk_level,
            "risk_color": risk.risk_color,
            "average_arrival_time": fmt_arr(sim.average_arrival_min),
            "best_case_arrival": fmt_arr(sim.best_case_arrival_min),
            "worst_case_arrival": fmt_arr(sim.worst_case_arrival_min),
            "arrival_std_min": sim.std_arrival_min,
            "main_risk_factor": risk.main_risk_factor,
            "vulnerable_leg": risk.vulnerable_leg,
            "tightest_buffer_description": risk.tightest_buffer_description,
            "sensitivity_explanation": risk.sensitivity_explanation,
            "full_explanation": risk.full_explanation,
            "recommendation_score": risk.recommendation_score,
            "arrival_distribution": sim.arrival_distribution,
        })

    options_out.sort(key=lambda x: -x["recommendation_score"])
    return {
        "journey_options": options_out,
        "recommended": options_out[0]["type"] if options_out else None,
        "source": src,
        "destination": dst,
        "source_city": CITIES[src]["name"],
        "destination_city": CITIES[dst]["name"],
        "distance_km": route["distance_km"],
        "departure_time": departure_time,
        "deadline_time": deadline_time,
        "simulation_runs": n_sims,
    }

@app.get("/health")
def health(): return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


from fastapi import FastAPI
from pydantic import BaseModel

from ml_engine import predict_reliability


app = FastAPI()


class JourneyInput(BaseModel):

    distance_km: float
    total_base_time_min: float
    total_buffer_min: float
    total_variance_min: float
    total_cost_inr: float
    n_legs: int
    has_flight: int
    has_train: int
    tightest_buffer_ratio: float
    max_leg_variance_min: float
    min_buffer_min: float
    variance_pct_of_base: float
    buffer_pct_of_base: float
    deadline_multiplier: float
    option_type_enc: int

    src_delhi: int
    src_lucknow: int
    src_chandigarh: int
    src_jaipur: int
    src_pune: int

    dst_delhi: int
    dst_lucknow: int
    dst_chandigarh: int
    dst_jaipur: int
    dst_pune: int

    std_arrival_min: float
    mean_final_delay_min: float
    risk_level_enc: int


@app.post("/predict")
def predict(data: JourneyInput):

    data_dict = data.dict()

    prob = predict_reliability(data_dict)

    # Risk logic
    if prob > 80:
        risk = "Low"
    elif prob > 60:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "reliability_percent": prob,
        "risk_level": risk
    }