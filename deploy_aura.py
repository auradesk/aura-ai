import requests
import time
import json
import os
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "aura_alerts.log")

os.makedirs(LOG_FOLDER, exist_ok=True)


def log_alert(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    full_message = f"[{timestamp}] {message}"

    print(full_message)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(full_message + "\n")


def post_request(endpoint, payload):

    url = BASE_URL + endpoint

    try:

        response = requests.post(url, json=payload, timeout=10)

        return response.json()

    except Exception as e:

        log_alert(f"Request failed: {e}")

        return None


def deploy():

    print("Starting Aura deployment...")

    payload = {

        "global_mission": "Full autonomous multi-domain optimization",

        "systems_final_status": [

            {
                "system_name": "Hospital Management",
                "final_score": 0.965,
                "status": "Operational"
            }

        ],

        "systems": [

            {
                "domain_name": "Hospital",
                "system_name": "Hospital Management",
                "readiness_score": 0.96
            }

        ]
    }

    result = post_request("/phase121/assess", payload)

    if result:

        print(json.dumps(result, indent=2))

    else:

        log_alert("Deployment failed")


def main():

    try:

        while True:

            deploy()

            time.sleep(30)

    except KeyboardInterrupt:

        print("Stopped safely")


if __name__ == "__main__":

    main()