# SureTrip v3 — Multi-City Reliability Intelligence

> Journey reliability quantified across 5 cities and 10 routes.
> Delhi · Lucknow · Chandigarh · Jaipur · Pune

---

## What's New in v3

| Feature | v2 | v3 |
|---|---|---|
| Cities | Delhi ↔ Lucknow only | **5 cities: Delhi, Lucknow, Chandigarh, Jaipur, Pune** |
| Routes | 1 bidirectional | **10 bidirectional combinations (5C2)** |
| Data | Hardcoded estimates | **Realistic data from IRails/DGCA/NH distances** |
| Buffer model | Fixed values | **Variance-proportional: buffer = f(variance)** |
| Database | Flat tables | **Multi-city schema: Cities, Routes, RouteOptions, TransportModes** |
| Map | Fixed Delhi-Lucknow | **Dynamic centering based on selected city pair** |
| UI | Fixed dropdowns | **Dynamic city selection with route preview** |

---

## ⚡ Quick Start

```bash
# Open frontend directly — zero setup required
open frontend/index.html
```

The complete simulation engine runs client-side in JavaScript.

---

## 🐍 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

---

## 🗺 Supported Routes (All 10 Combinations)

| Route | Distance | Fastest Option | Cheapest | Most Reliable |
|---|---|---|---|---|
| Delhi ↔ Lucknow | 556 km | Flight ~3.5hr | Bus ~9hr ₹595 | Shatabdi ~7.5hr |
| Delhi ↔ Chandigarh | 250 km | Volvo Bus ~5hr | State Bus ₹445 | Shatabdi ~4hr |
| Delhi ↔ Jaipur | 270 km | Cab NH-48 ~4.5hr | Roadways ₹385 | Shatabdi ~5hr |
| Delhi ↔ Pune | 1408 km | Flight ~3.5hr | Train ~24hr ₹1260 | Flight (reliable) |
| Lucknow ↔ Chandigarh | 600 km | Via-Delhi flight | Overnight bus ₹900 | Chandigarh Express |
| Lucknow ↔ Jaipur | 630 km | Direct flight | Mail train ₹740 | Express train |
| Lucknow ↔ Pune | 1400 km | Direct flight | Express train ₹1210 | Flight (reliable) |
| Chandigarh ↔ Jaipur | 540 km | Volvo Bus | State bus ₹730 | Train via Delhi |
| Chandigarh ↔ Pune | 1650 km | Flight (1-stop) | Train ₹1610 | Flight (reliable) |
| Jaipur ↔ Pune | 1150 km | Direct flight | Train ₹1050 | Flight (reliable) |

---

## 📊 Data Sources

All transport parameters are based on publicly available averages:

| Mode | Source |
|---|---|
| Train times | Indian Railways NTES timetables (Shatabdi, Rajdhani, Mail Express) |
| Flight durations | DGCA domestic route averages + airport overhead |
| Road times | NH distance charts + avg speed on national highways |
| Bus times | HRTC, RSRTC, MSRTC timetable averages |
| Costs | Ola/Uber city averages, IRCTC fare tables, airline average fares |
| Variance | IRails delay stats, DGCA punctuality reports (approximated) |

---

## 🎲 Simulation Model

### Delay Propagation (Core Innovation)

```
for each simulation run:
  carried_delay ← 0

  for each leg_i:
    raw_delay ← Normal(0, variance_i)        [clipped to -0.5σ … +2.5σ]
    overflow_i = max(0, carried_delay + raw_delay - buffer_i)
    carried_delay ← overflow_i               ← cascades to next leg

  arrival = Σ(base_time_i) + Σ(buffer_i) + carried_delay - last_buffer
  success = arrival ≤ deadline
```

### Buffer Sizing Rule

Buffer is sized proportional to variance — not a fixed constant:
- `buffer = (variance × 0.6) + fixed_transfer_time`
- Short urban legs: 15–20 min buffers
- Long intercity: 20–35 min buffers
- Flight connections: 20–25 min (checked in downstream)

### Risk Classification

| Probability | Risk | Color |
|---|---|---|
| ≥ 80% | Low | 🟢 Green |
| 60–79% | Medium | 🟡 Yellow |
| < 60% | High | 🔴 Red |

### Recommendation Score
```
score = reliability × 0.60 + speed_score × 0.25 + cost_score × 0.15
```

---

## 🔌 API Reference

### `POST /plan-journey`

```
POST /plan-journey?source=delhi&destination=pune&departure_time=2024-03-15T08:00:00&deadline_time=2024-03-15T14:00:00&n_simulations=1000
```

**Response:**
```json
{
  "journey_options": [{
    "type": "Most Reliable",
    "probability_of_success": 84.3,
    "probability_of_failure": 15.7,
    "risk_level": "Low",
    "average_arrival_time": "13:22, 15 Mar",
    "best_case_arrival": "13:05, 15 Mar",
    "worst_case_arrival": "14:18, 15 Mar",
    "main_risk_factor": "...",
    "vulnerable_leg": "...",
    "sensitivity_explanation": "..."
  }],
  "recommended": "Most Reliable",
  "distance_km": 1408
}
```

### `GET /cities` — List all cities with coordinates
### `GET /routes` — List all route combinations with distances

---

## 📁 Project Structure

```
suretrip_v3/
├── backend/
│   ├── main.py                  # FastAPI app
│   ├── simulation_engine.py     # Core Monte Carlo with propagation
│   ├── risk_analysis.py         # Risk classifier and explainer
│   ├── models.py                # SQLAlchemy ORM models
│   ├── database.py              # DB config
│   └── requirements.txt
│
├── database/
│   └── seed_data.py             # All cities, routes, transport data
│
├── frontend/
│   ├── index.html               # Complete self-contained app
│   └── app.js                   # Simulation + rendering engine
│
├── docker-compose.yml
└── README.md
```

---

## 🗺 Google Maps Integration Note

The `GOOGLE_MAPS_API_KEY` in `.env.template` is provided for future upgrade.
Current map uses **OpenStreetMap + CartoDB dark tiles via Leaflet** — no API key needed.

To upgrade to Google Maps:
1. Add `GOOGLE_MAPS_API_KEY` to `.env`
2. Replace Leaflet tile layer with Google Maps API initialization
3. Keep all reliability logic unchanged — Google Maps is visualization only

---


