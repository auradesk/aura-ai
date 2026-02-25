from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import threading
import time
import requests

app = FastAPI(title="Aura AI Professional Control Center")

AURA_CORE_URL = "http://127.0.0.1:8000/phase121/assess"
REFRESH_INTERVAL = 5  # seconds

# Cache for live data
system_cache = {"systems_final_status": []}

# Map systems to domains
DOMAIN_MAPPING = {
    "Hospital": "Healthcare",
    "Pharmacy": "Healthcare",
    "School": "Education",
    "LMS": "Education"
}


def fetch_live_status():
    while True:
        try:
            payload = {
                "global_mission": "Autonomous Multi-Domain Optimization",
                "systems": system_cache.get("systems_final_status", []),
                "systems_final_status": system_cache.get("systems_final_status", [])
            }
            resp = requests.post(AURA_CORE_URL, json=payload, timeout=2)
            if resp.status_code == 200:
                data = resp.json()
                systems = data.get("systems_final_status", [])
                # Apply domain mapping
                for s in systems:
                    name = s.get("system_name", "Unknown")
                    s["domain_name"] = DOMAIN_MAPPING.get(name, s.get("domain_name", "Business"))
                    # Ensure all expected fields exist
                    s.setdefault("status", "Unknown")
                    s.setdefault("final_score", 0)
                    s.setdefault("efficiency_score", "N/A")
                    s.setdefault("knowledge_score", "N/A")
                    s.setdefault("innovation_score", "N/A")
                    s.setdefault("risk_mitigation_score", "N/A")
                    s.setdefault("adaptation_score", "N/A")
                    s.setdefault("deployment_confidence", "N/A")
                system_cache["systems_final_status"] = systems
                print("[DEBUG] Fetched systems:", systems)
        except Exception as e:
            print(f"[Warning] Could not fetch live status: {e}")
        time.sleep(REFRESH_INTERVAL)


threading.Thread(target=fetch_live_status, daemon=True).start()


@app.get("/", response_class=HTMLResponse)
def dashboard():
    systems = system_cache.get("systems_final_status", [])
    if not systems:
        return HTMLResponse("""
            <h1>Aura AI Professional Control Center</h1>
            <h2>Status: ACTIVE | Live Refresh Every 5s</h2>
            <p>Waiting for live system data from Aura Core...</p>
        """)

    # Group by domain
    grouped = {}
    for s in systems:
        domain = s.get("domain_name", "Business")
        grouped.setdefault(domain, []).append(s)

    html = """
    <html>
    <head>
        <title>Aura AI Professional Dashboard</title>
        <style>
            body {font-family: Arial; background:#0f172a; color:white; margin:0; padding:0;}
            h1 {text-align:center; margin:20px;}
            h2 {text-align:center; margin-bottom:5px;}
            .domain {margin:20px; padding:20px; background:#1e293b; border-radius:10px;}
            .domain h2 {color:#38bdf8; margin-top:0;}
            .system {padding:15px; margin:10px 0; background:#334155; border-radius:8px; cursor:pointer; transition:0.3s;}
            .system:hover {background:#475569;}
            .metrics {display:none; padding-top:10px;}
            .score-good {color:#22c55e; font-weight:bold;}
            .score-warning {color:#facc15; font-weight:bold;}
            .score-critical {color:#f87171; font-weight:bold;}
            .alerts {margin:20px; padding:15px; background:#991b1b; border-radius:8px;}
            .toggle {float:right; color:#38bdf8; cursor:pointer;}
        </style>
        <meta http-equiv="refresh" content="5">
        <script>
            function toggleMetrics(id){
                var e = document.getElementById(id);
                e.style.display = (e.style.display === 'block') ? 'none' : 'block';
            }
        </script>
    </head>
    <body>
        <h1>Aura AI Professional Control Center</h1>
        <h2>Status: ACTIVE | Live Refresh Every 5s</h2>
    """

    # Alerts
    alerts = []
    for s in systems:
        final_score = s.get("final_score", 0)
        if final_score < 0.85:
            alerts.append(f"{s.get('system_name')} ({s.get('domain_name')}) is CRITICAL!")
        elif final_score < 0.95:
            alerts.append(f"{s.get('system_name')} ({s.get('domain_name')}) WARNING.")

    if alerts:
        html += "<div class='alerts'><b>Alerts:</b><br>" + "<br>".join(alerts) + "</div>"

    # Render domains
    for domain in ["Healthcare", "Education", "Business"]:
        sys_list = grouped.get(domain, [])
        if not sys_list:
            continue
        html += f"<div class='domain'><h2>{domain}</h2>"
        for idx, s in enumerate(sys_list):
            final_score = s.get("final_score", 0)
            if final_score < 0.85:
                score_class = "score-critical"
            elif final_score < 0.95:
                score_class = "score-warning"
            else:
                score_class = "score-good"

            html += f"""
            <div class='system' onclick="toggleMetrics('metrics{domain}{idx}')">
                <b>{s.get('system_name')}</b> | Final Score: <span class='{score_class}'>{final_score}</span>
                <span class='toggle'>[Details]</span>
                <div class='metrics' id='metrics{domain}{idx}'>
                    Status: {s.get('status')}<br>
                    Efficiency: {s.get('efficiency_score')} | Knowledge: {s.get('knowledge_score')} | Innovation: {s.get('innovation_score')} | Risk Mitigation: {s.get('risk_mitigation_score')}<br>
                    Adaptation: {s.get('adaptation_score')} | Deployment Confidence: {s.get('deployment_confidence')}
                </div>
            </div>
            """
        html += "</div>"

    html += "</body></html>"
    return html