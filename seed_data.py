"""
SureTrip v3 — Seed Data
========================
Realistic transport data based on public averages:
- Indian Railways timetables
- DGCA domestic flight data
- NH distance charts
- Urban traffic studies

Cities: Delhi, Lucknow, Chandigarh, Jaipur, Pune
Routes: All 10 bidirectional combinations (5C2 = 10)
"""

CITIES = {
    "delhi": {
        "name": "Delhi",
        "lat": 28.6139, "lon": 77.2090,
        "code": "DEL",
        "emoji": "🏛",
        "hubs": {
            "home":            {"name": "Connaught Place",                    "lat": 28.6315, "lon": 77.2167},
            "railway_station": {"name": "New Delhi Railway Station (NDLS)",   "lat": 28.6419, "lon": 77.2195},
            "airport":         {"name": "Indira Gandhi Intl Airport (IGI)",   "lat": 28.5562, "lon": 77.1000},
            "bus_terminal":    {"name": "Kashmere Gate ISBT",                 "lat": 28.6670, "lon": 77.2286},
            "metro_station":   {"name": "Rajiv Chowk Metro Station",          "lat": 28.6328, "lon": 77.2197},
        }
    },
    "lucknow": {
        "name": "Lucknow",
        "lat": 26.8467, "lon": 80.9462,
        "code": "LKO",
        "emoji": "🕌",
        "hubs": {
            "home":            {"name": "Hazratganj",                         "lat": 26.8467, "lon": 80.9462},
            "railway_station": {"name": "Charbagh Railway Station",           "lat": 26.8467, "lon": 80.9148},
            "airport":         {"name": "Chaudhary Charan Singh Airport",     "lat": 26.7606, "lon": 80.8893},
            "bus_terminal":    {"name": "Alambagh Bus Terminal",              "lat": 26.8004, "lon": 80.9014},
            "metro_station":   {"name": "Hazratganj Metro Station",           "lat": 26.8467, "lon": 80.9462},
        }
    },
    "chandigarh": {
        "name": "Chandigarh",
        "lat": 30.7333, "lon": 76.7794,
        "code": "IXC",
        "emoji": "🌿",
        "hubs": {
            "home":            {"name": "Sector 17 Plaza",                    "lat": 30.7417, "lon": 76.7882},
            "railway_station": {"name": "Chandigarh Railway Station",         "lat": 30.7090, "lon": 76.8020},
            "airport":         {"name": "Chandigarh International Airport",   "lat": 30.6735, "lon": 76.7885},
            "bus_terminal":    {"name": "ISBT Sector 43",                    "lat": 30.7074, "lon": 76.7908},
            "metro_station":   {"name": "N/A — No Metro (Cab/Bus feeder)",   "lat": 30.7333, "lon": 76.7794},
        }
    },
    "jaipur": {
        "name": "Jaipur",
        "lat": 26.9124, "lon": 75.7873,
        "code": "JAI",
        "emoji": "🏰",
        "hubs": {
            "home":            {"name": "MI Road / City Center",              "lat": 26.9199, "lon": 75.8162},
            "railway_station": {"name": "Jaipur Junction Railway Station",    "lat": 26.9215, "lon": 75.7873},
            "airport":         {"name": "Jaipur International Airport (JAI)", "lat": 26.8242, "lon": 75.8122},
            "bus_terminal":    {"name": "Sindhi Camp Bus Stand",              "lat": 26.9185, "lon": 75.7970},
            "metro_station":   {"name": "Chandpole Metro Station",            "lat": 26.9228, "lon": 75.8078},
        }
    },
    "pune": {
        "name": "Pune",
        "lat": 18.5204, "lon": 73.8567,
        "code": "PNQ",
        "emoji": "🎓",
        "hubs": {
            "home":            {"name": "Shivajinagar / FC Road",             "lat": 18.5314, "lon": 73.8446},
            "railway_station": {"name": "Pune Junction Railway Station",      "lat": 18.5279, "lon": 73.8742},
            "airport":         {"name": "Pune Airport (PNQ)",                 "lat": 18.5822, "lon": 73.9197},
            "bus_terminal":    {"name": "Swargate Bus Terminal",              "lat": 18.5018, "lon": 73.8636},
            "metro_station":   {"name": "Shivajinagar Metro Station",         "lat": 18.5314, "lon": 73.8446},
        }
    },
}


TRANSPORT_MODES = {
    "metro": {
        "name": "Metro",
        "icon": "🚇",
        "color": "#3b82f6",
        "avg_speed_kmph": 35,
        "base_cost_per_km": 2.5,
        "variance_factor": 0.18,   
        "fixed_variance": 7,        
        "notes": "Signal-controlled; very consistent"
    },
    "cab": {
        "name": "Cab",
        "icon": "🚕",
        "color": "#f59e0b",
        "avg_speed_kmph": 28,
        "base_cost_per_km": 14,
        "variance_factor": 0.35,
        "fixed_variance": 12,
        "notes": "Traffic-sensitive; Ola/Uber pricing"
    },
    "auto": {
        "name": "Auto Rickshaw",
        "icon": "🛺",
        "color": "#10b981",
        "avg_speed_kmph": 22,
        "base_cost_per_km": 10,
        "variance_factor": 0.30,
        "fixed_variance": 8,
        "notes": "Urban short-distance; moderate variance"
    },
    "dtc_bus": {
        "name": "City Bus",
        "icon": "🚌",
        "color": "#8b5cf6",
        "avg_speed_kmph": 20,
        "base_cost_per_km": 1.5,
        "variance_factor": 0.30,
        "fixed_variance": 12,
        "notes": "City buses; traffic + stop delays"
    },
    "express_train": {
        "name": "Express Train",
        "icon": "🚄",
        "color": "#06b6d4",
        "avg_speed_kmph": 90,
        "base_cost_per_km": 1.8,
        "variance_factor": 0.08,
        "fixed_variance": 15,
        "notes": "Shatabdi/Rajdhani class; fewer stops"
    },
    "mail_train": {
        "name": "Mail/Express Train",
        "icon": "🚂",
        "color": "#64748b",
        "avg_speed_kmph": 65,
        "base_cost_per_km": 1.2,
        "variance_factor": 0.12,
        "fixed_variance": 20,
        "notes": "Regular express; crossing waits"
    },
    "flight": {
        "name": "Flight",
        "icon": "✈️",
        "color": "#ef4444",
        "avg_speed_kmph": 750,
        "base_cost_per_km": 6.5,
        "variance_factor": 0.22,
        "fixed_variance": 18,
        "notes": "ATC, boarding, taxi-queue uncertainty"
    },
    "intercity_bus": {
        "name": "Intercity Bus",
        "icon": "🚎",
        "color": "#d97706",
        "avg_speed_kmph": 55,
        "base_cost_per_km": 1.0,
        "variance_factor": 0.14,
        "fixed_variance": 25,
        "notes": "NH traffic, rest stops, driver changeovers"
    },
    "volvo_bus": {
        "name": "Volvo/AC Bus",
        "icon": "🚐",
        "color": "#7c3aed",
        "avg_speed_kmph": 65,
        "base_cost_per_km": 1.6,
        "variance_factor": 0.12,
        "fixed_variance": 20,
        "notes": "Premium intercity AC bus"
    },
}



ROUTES = {

    ("delhi", "lucknow"): {
        "distance_km": 556,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Metro to IGI + Flight + Cab — 3.5-4hr total including transfers",
            "legs": [
                {"mode": "metro",   "from": "delhi.home",      "to": "delhi.airport",   "base_time": 45,  "variance": 9,  "buffer": 15, "cost": 60},
                {"mode": "flight",  "from": "delhi.airport",   "to": "lucknow.airport", "base_time": 65,  "variance": 20, "buffer": 20, "cost": 4200},
                {"mode": "cab",     "from": "lucknow.airport", "to": "lucknow.home",    "base_time": 35,  "variance": 12, "buffer": 0,  "cost": 350},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "City bus + Intercity sleeper bus — overnight option, lowest cost",
            "legs": [
                {"mode": "dtc_bus",       "from": "delhi.home",          "to": "delhi.bus_terminal",    "base_time": 50,  "variance": 14, "buffer": 20, "cost": 25},
                {"mode": "intercity_bus", "from": "delhi.bus_terminal",  "to": "lucknow.bus_terminal",  "base_time": 480, "variance": 55, "buffer": 15, "cost": 450},
                {"mode": "auto",          "from": "lucknow.bus_terminal", "to": "lucknow.home",         "base_time": 25,  "variance": 9,  "buffer": 0,  "cost": 120},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Metro + Shatabdi Express + Metro — best on-time record for this corridor",
            "legs": [
                {"mode": "metro",         "from": "delhi.home",          "to": "delhi.railway_station", "base_time": 20,  "variance": 7,  "buffer": 30, "cost": 30},
                {"mode": "express_train", "from": "delhi.railway_station","to": "lucknow.railway_station","base_time": 390, "variance": 25, "buffer": 25, "cost": 650},
                {"mode": "metro",         "from": "lucknow.metro_station","to": "lucknow.home",          "base_time": 12,  "variance": 5,  "buffer": 0,  "cost": 20},
            ]
        }
    },

    
    ("delhi", "chandigarh"): {
        "distance_km": 250,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Volvo AC Bus via NH-44 — faster than train with less transfer overhead",
            "legs": [
                {"mode": "cab",       "from": "delhi.home",          "to": "delhi.bus_terminal",      "base_time": 35,  "variance": 14, "buffer": 15, "cost": 280},
                {"mode": "volvo_bus", "from": "delhi.bus_terminal",  "to": "chandigarh.bus_terminal", "base_time": 240, "variance": 28, "buffer": 10, "cost": 600},
                {"mode": "cab",       "from": "chandigarh.bus_terminal","to": "chandigarh.home",      "base_time": 20,  "variance": 8,  "buffer": 0,  "cost": 200},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "City bus + Intercity bus — most affordable NH-44 corridor option",
            "legs": [
                {"mode": "dtc_bus",       "from": "delhi.home",          "to": "delhi.bus_terminal",      "base_time": 50,  "variance": 14, "buffer": 20, "cost": 25},
                {"mode": "intercity_bus", "from": "delhi.bus_terminal",  "to": "chandigarh.bus_terminal", "base_time": 270, "variance": 32, "buffer": 15, "cost": 320},
                {"mode": "auto",          "from": "chandigarh.bus_terminal","to": "chandigarh.home",       "base_time": 18,  "variance": 7,  "buffer": 0,  "cost": 100},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Metro + Shatabdi Express — fixed departure, good punctuality on this route",
            "legs": [
                {"mode": "metro",         "from": "delhi.home",          "to": "delhi.railway_station",     "base_time": 20,  "variance": 7,  "buffer": 30, "cost": 30},
                {"mode": "express_train", "from": "delhi.railway_station","to": "chandigarh.railway_station","base_time": 210, "variance": 18, "buffer": 20, "cost": 520},
                {"mode": "cab",           "from": "chandigarh.railway_station","to": "chandigarh.home",     "base_time": 18,  "variance": 7,  "buffer": 0,  "cost": 180},
            ]
        }
    },

    
    ("delhi", "jaipur"): {
        "distance_km": 270,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Cab via NH-48 (Jaipur Expressway) — no terminal overhead, direct city-to-city",
            "legs": [
                {"mode": "cab", "from": "delhi.home", "to": "jaipur.home",
                 "base_time": 270, "variance": 38, "buffer": 0, "cost": 3200},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "City bus + Rajasthan Roadways — cheapest on this short-to-medium corridor",
            "legs": [
                {"mode": "dtc_bus",       "from": "delhi.home",         "to": "delhi.bus_terminal",   "base_time": 50,  "variance": 14, "buffer": 20, "cost": 25},
                {"mode": "intercity_bus", "from": "delhi.bus_terminal", "to": "jaipur.bus_terminal",  "base_time": 300, "variance": 38, "buffer": 10, "cost": 280},
                {"mode": "auto",          "from": "jaipur.bus_terminal","to": "jaipur.home",           "base_time": 20,  "variance": 8,  "buffer": 0,  "cost": 80},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Metro + Shatabdi/Intercity Express — structured schedule with high punctuality",
            "legs": [
                {"mode": "metro",         "from": "delhi.home",          "to": "delhi.railway_station", "base_time": 20,  "variance": 7,  "buffer": 30, "cost": 30},
                {"mode": "express_train", "from": "delhi.railway_station","to": "jaipur.railway_station","base_time": 270, "variance": 20, "buffer": 20, "cost": 480},
                {"mode": "cab",           "from": "jaipur.railway_station","to": "jaipur.home",          "base_time": 12,  "variance": 6,  "buffer": 0,  "cost": 120},
            ]
        }
    },

    
    ("delhi", "pune"): {
        "distance_km": 1408,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Metro + Flight + Metro — only practical fast option for this 1400km corridor",
            "legs": [
                {"mode": "metro",  "from": "delhi.home",    "to": "delhi.airport",  "base_time": 45,  "variance": 9,  "buffer": 15, "cost": 60},
                {"mode": "flight", "from": "delhi.airport", "to": "pune.airport",   "base_time": 120, "variance": 25, "buffer": 25, "cost": 5500},
                {"mode": "cab",    "from": "pune.airport",  "to": "pune.home",      "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "Metro + Rajdhani/Express Train — long but most economical for 1400km",
            "legs": [
                {"mode": "metro",      "from": "delhi.home",           "to": "delhi.railway_station", "base_time": 20,  "variance": 7,  "buffer": 30, "cost": 30},
                {"mode": "mail_train", "from": "delhi.railway_station","to": "pune.railway_station",  "base_time": 1380,"variance": 80, "buffer": 30, "cost": 1200},
                {"mode": "metro",      "from": "pune.railway_station", "to": "pune.home",             "base_time": 20,  "variance": 10, "buffer": 0,  "cost": 30},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Metro + Flight + Cab — flight is most reliable for long haul; generous airport buffers",
            "legs": [
                {"mode": "metro",  "from": "delhi.home",    "to": "delhi.airport",  "base_time": 45,  "variance": 9,  "buffer": 20, "cost": 60},
                {"mode": "flight", "from": "delhi.airport", "to": "pune.airport",   "base_time": 120, "variance": 22, "buffer": 25, "cost": 5800},
                {"mode": "cab",    "from": "pune.airport",  "to": "pune.home",      "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        }
    },

    
    ("lucknow", "chandigarh"): {
        "distance_km": 600,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Cab + Flight via Delhi + Cab — no direct flight; 1-stop via IGI",
            "legs": [
                {"mode": "cab",    "from": "lucknow.home",   "to": "lucknow.airport",   "base_time": 40,  "variance": 14, "buffer": 20, "cost": 380},
                {"mode": "flight", "from": "lucknow.airport","to": "delhi.airport",      "base_time": 65,  "variance": 20, "buffer": 60, "cost": 3200},
                {"mode": "flight", "from": "delhi.airport",  "to": "chandigarh.airport", "base_time": 45,  "variance": 16, "buffer": 15, "cost": 2800},
                {"mode": "cab",    "from": "chandigarh.airport","to": "chandigarh.home", "base_time": 25,  "variance": 9,  "buffer": 0,  "cost": 220},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "Auto + Overnight bus (direct Lucknow–Chandigarh) — cheapest option",
            "legs": [
                {"mode": "auto",          "from": "lucknow.home",        "to": "lucknow.bus_terminal",    "base_time": 25,  "variance": 9,  "buffer": 20, "cost": 100},
                {"mode": "intercity_bus", "from": "lucknow.bus_terminal","to": "chandigarh.bus_terminal", "base_time": 600, "variance": 65, "buffer": 20, "cost": 700},
                {"mode": "auto",          "from": "chandigarh.bus_terminal","to": "chandigarh.home",      "base_time": 18,  "variance": 7,  "buffer": 0,  "cost": 100},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Auto + Express Train (Chandigarh Express) — direct rail, structured schedule",
            "legs": [
                {"mode": "auto",          "from": "lucknow.home",         "to": "lucknow.railway_station",    "base_time": 20,  "variance": 8,  "buffer": 35, "cost": 80},
                {"mode": "express_train", "from": "lucknow.railway_station","to": "chandigarh.railway_station","base_time": 660, "variance": 40, "buffer": 20, "cost": 750},
                {"mode": "cab",           "from": "chandigarh.railway_station","to": "chandigarh.home",        "base_time": 18,  "variance": 7,  "buffer": 0,  "cost": 180},
            ]
        }
    },

    
    ("lucknow", "jaipur"): {
        "distance_km": 630,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Cab + Direct flight (Lucknow–Jaipur, limited frequency) + Cab",
            "legs": [
                {"mode": "cab",    "from": "lucknow.home",    "to": "lucknow.airport", "base_time": 40,  "variance": 14, "buffer": 20, "cost": 380},
                {"mode": "flight", "from": "lucknow.airport", "to": "jaipur.airport",  "base_time": 80,  "variance": 22, "buffer": 20, "cost": 4500},
                {"mode": "cab",    "from": "jaipur.airport",  "to": "jaipur.home",     "base_time": 25,  "variance": 10, "buffer": 0,  "cost": 300},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "Auto + Mail/Express train — direct LKO–JP route, good value",
            "legs": [
                {"mode": "auto",       "from": "lucknow.home",          "to": "lucknow.railway_station", "base_time": 20,  "variance": 8,  "buffer": 35, "cost": 80},
                {"mode": "mail_train", "from": "lucknow.railway_station","to": "jaipur.railway_station",  "base_time": 600, "variance": 55, "buffer": 20, "cost": 580},
                {"mode": "auto",       "from": "jaipur.railway_station", "to": "jaipur.home",             "base_time": 12,  "variance": 6,  "buffer": 0,  "cost": 80},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Auto + Express train with extra buffer — more reliable schedule than mail train",
            "legs": [
                {"mode": "auto",          "from": "lucknow.home",          "to": "lucknow.railway_station", "base_time": 20,  "variance": 8,  "buffer": 35, "cost": 80},
                {"mode": "express_train", "from": "lucknow.railway_station","to": "jaipur.railway_station",  "base_time": 560, "variance": 38, "buffer": 25, "cost": 780},
                {"mode": "cab",           "from": "jaipur.railway_station", "to": "jaipur.home",             "base_time": 12,  "variance": 6,  "buffer": 0,  "cost": 120},
            ]
        }
    },

   
    ("lucknow", "pune"): {
        "distance_km": 1400,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Cab + Direct flight (Lucknow–Pune, IndiGo/SpiceJet) + Cab",
            "legs": [
                {"mode": "cab",    "from": "lucknow.home",    "to": "lucknow.airport", "base_time": 40,  "variance": 14, "buffer": 20, "cost": 380},
                {"mode": "flight", "from": "lucknow.airport", "to": "pune.airport",    "base_time": 110, "variance": 24, "buffer": 20, "cost": 5200},
                {"mode": "cab",    "from": "pune.airport",    "to": "pune.home",       "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "Auto + Long-distance Express train — most economical for 1400km route",
            "legs": [
                {"mode": "auto",       "from": "lucknow.home",          "to": "lucknow.railway_station", "base_time": 20,  "variance": 8,  "buffer": 30, "cost": 80},
                {"mode": "mail_train", "from": "lucknow.railway_station","to": "pune.railway_station",    "base_time": 1320,"variance": 75, "buffer": 30, "cost": 1100},
                {"mode": "metro",      "from": "pune.railway_station",  "to": "pune.home",               "base_time": 20,  "variance": 10, "buffer": 0,  "cost": 30},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Cab + Flight + Cab — only practical reliable option for 1400km; generous airport buffers",
            "legs": [
                {"mode": "cab",    "from": "lucknow.home",    "to": "lucknow.airport", "base_time": 40,  "variance": 14, "buffer": 25, "cost": 380},
                {"mode": "flight", "from": "lucknow.airport", "to": "pune.airport",    "base_time": 110, "variance": 22, "buffer": 25, "cost": 5500},
                {"mode": "cab",    "from": "pune.airport",    "to": "pune.home",       "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        }
    },

    
    ("chandigarh", "jaipur"): {
        "distance_km": 540,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Volvo AC Bus via NH-48 — direct overnight/daytime, beats train+metro overhead",
            "legs": [
                {"mode": "cab",       "from": "chandigarh.home",       "to": "chandigarh.bus_terminal", "base_time": 22,  "variance": 8,  "buffer": 15, "cost": 200},
                {"mode": "volvo_bus", "from": "chandigarh.bus_terminal","to": "jaipur.bus_terminal",     "base_time": 480, "variance": 50, "buffer": 10, "cost": 800},
                {"mode": "cab",       "from": "jaipur.bus_terminal",   "to": "jaipur.home",             "base_time": 15,  "variance": 7,  "buffer": 0,  "cost": 120},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "Auto + State bus (Chandigarh to Jaipur) — cheapest direct intercity option",
            "legs": [
                {"mode": "auto",          "from": "chandigarh.home",       "to": "chandigarh.bus_terminal", "base_time": 20,  "variance": 7,  "buffer": 20, "cost": 100},
                {"mode": "intercity_bus", "from": "chandigarh.bus_terminal","to": "jaipur.bus_terminal",     "base_time": 510, "variance": 55, "buffer": 15, "cost": 550},
                {"mode": "auto",          "from": "jaipur.bus_terminal",   "to": "jaipur.home",             "base_time": 15,  "variance": 7,  "buffer": 0,  "cost": 80},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Cab + Express Train (via Delhi) — train is most predictable despite longer routing",
            "legs": [
                {"mode": "cab",           "from": "chandigarh.home",          "to": "chandigarh.railway_station", "base_time": 20,  "variance": 8,  "buffer": 35, "cost": 180},
                {"mode": "express_train", "from": "chandigarh.railway_station","to": "jaipur.railway_station",     "base_time": 720, "variance": 45, "buffer": 25, "cost": 860},
                {"mode": "cab",           "from": "jaipur.railway_station",   "to": "jaipur.home",                "base_time": 12,  "variance": 6,  "buffer": 0,  "cost": 120},
            ]
        }
    },

    
    ("chandigarh", "pune"): {
        "distance_km": 1650,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Cab + Flight (1-stop via Delhi or Mumbai) + Cab — only practical option",
            "legs": [
                {"mode": "cab",    "from": "chandigarh.home",    "to": "chandigarh.airport", "base_time": 28,  "variance": 10, "buffer": 20, "cost": 280},
                {"mode": "flight", "from": "chandigarh.airport", "to": "pune.airport",       "base_time": 155, "variance": 28, "buffer": 20, "cost": 6200},
                {"mode": "cab",    "from": "pune.airport",       "to": "pune.home",          "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "Cab + Long-distance train (via Delhi) — slow but very affordable for 1650km",
            "legs": [
                {"mode": "cab",        "from": "chandigarh.home",          "to": "chandigarh.railway_station", "base_time": 20,  "variance": 8,  "buffer": 35, "cost": 180},
                {"mode": "mail_train", "from": "chandigarh.railway_station","to": "pune.railway_station",       "base_time": 1680,"variance": 95, "buffer": 30, "cost": 1400},
                {"mode": "metro",      "from": "pune.railway_station",     "to": "pune.home",                  "base_time": 20,  "variance": 10, "buffer": 0,  "cost": 30},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Cab + Flight + Cab — only reliable option for 1650km; train variance is prohibitively high",
            "legs": [
                {"mode": "cab",    "from": "chandigarh.home",    "to": "chandigarh.airport", "base_time": 28,  "variance": 10, "buffer": 20, "cost": 280},
                {"mode": "flight", "from": "chandigarh.airport", "to": "pune.airport",       "base_time": 155, "variance": 25, "buffer": 25, "cost": 6500},
                {"mode": "cab",    "from": "pune.airport",       "to": "pune.home",          "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        }
    },

    
    ("jaipur", "pune"): {
        "distance_km": 1150,
        "fastest": {
            "name": "Fastest", "icon": "⚡",
            "description": "Metro + Direct flight (Jaipur–Pune IndiGo) + Cab — ~4.5hr door-to-door",
            "legs": [
                {"mode": "metro",  "from": "jaipur.home",    "to": "jaipur.airport",  "base_time": 28,  "variance": 7,  "buffer": 15, "cost": 35},
                {"mode": "flight", "from": "jaipur.airport", "to": "pune.airport",    "base_time": 95,  "variance": 22, "buffer": 20, "cost": 4800},
                {"mode": "cab",    "from": "pune.airport",   "to": "pune.home",       "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        },
        "cheapest": {
            "name": "Cheapest", "icon": "💰",
            "description": "Cab + Express train (Jaipur–Pune Express) — long but affordable",
            "legs": [
                {"mode": "cab",        "from": "jaipur.home",          "to": "jaipur.railway_station", "base_time": 12,  "variance": 6,  "buffer": 35, "cost": 120},
                {"mode": "mail_train", "from": "jaipur.railway_station","to": "pune.railway_station",   "base_time": 960, "variance": 65, "buffer": 25, "cost": 900},
                {"mode": "metro",      "from": "pune.railway_station", "to": "pune.home",              "base_time": 20,  "variance": 10, "buffer": 0,  "cost": 30},
            ]
        },
        "reliable": {
            "name": "Most Reliable", "icon": "🛡",
            "description": "Metro + Flight + Cab — most reliable for 1150km; extra airport buffer reduces risk",
            "legs": [
                {"mode": "metro",  "from": "jaipur.home",    "to": "jaipur.airport",  "base_time": 28,  "variance": 7,  "buffer": 20, "cost": 35},
                {"mode": "flight", "from": "jaipur.airport", "to": "pune.airport",    "base_time": 95,  "variance": 20, "buffer": 25, "cost": 5100},
                {"mode": "cab",    "from": "pune.airport",   "to": "pune.home",       "base_time": 30,  "variance": 14, "buffer": 0,  "cost": 450},
            ]
        }
    },
}

def get_route(src: str, dst: str) -> dict:
    """Return route data for any city pair (handles reverse direction)."""
    key = (src, dst)
    rev = (dst, src)
    if key in ROUTES:
        return ROUTES[key]
    if rev in ROUTES:
        
        route = ROUTES[rev]
        reversed_route = {"distance_km": route["distance_km"]}
        for opt_key in ["fastest", "cheapest", "reliable"]:
            opt = route[opt_key]
            reversed_legs = []
            for leg in reversed(opt["legs"]):
                reversed_legs.append({
                    "mode": leg["mode"],
                    "from": leg["to"].replace(f"{dst}.", f"{src}.").replace(f"{src}.", f"{dst}.") if "." in leg["to"] else leg["to"],
                    "to":   leg["from"].replace(f"{dst}.", f"{src}.").replace(f"{src}.", f"{dst}.") if "." in leg["from"] else leg["from"],
                    "base_time": leg["base_time"],
                    "variance": leg["variance"],
                    "buffer": leg["buffer"],
                    "cost": leg["cost"],
                })
            reversed_route[opt_key] = {
                "name": opt["name"],
                "icon": opt["icon"],
                "description": opt["description"],
                "legs": reversed_legs,
            }
        return reversed_route
    raise KeyError(f"No route found for {src} ↔ {dst}")

def resolve_location(loc_key: str) -> dict:
    """Resolve 'city.hub_type' to coordinates and name."""
    parts = loc_key.split(".")
    if len(parts) != 2:
        return {"name": loc_key, "lat": 0, "lon": 0}
    city_key, hub_type = parts
    city = CITIES.get(city_key, {})
    hubs = city.get("hubs", {})
    hub = hubs.get(hub_type, {"name": loc_key, "lat": city.get("lat", 0), "lon": city.get("lon", 0)})
    return hub

CITY_LIST = list(CITIES.keys())
VALID_COMBINATIONS = [
    (CITY_LIST[i], CITY_LIST[j])
    for i in range(len(CITY_LIST))
    for j in range(i+1, len(CITY_LIST))
]
