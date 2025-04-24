from datetime import datetime
import requests
import random

# Simulated GPS module
def get_location():
    # Fake GPS location (Sagi Rama Krishnam Raju Engineering College, Bhimavaram)
    return 16.5449, 81.5212

# Default Webhook URLs for testing (You can change these later)
POLICE_ALERT_WEBHOOK = "https://webhook.site/1c68d7c7-1111-aaaa-bbbb-2222cc334455"
OWNER_ALERT_WEBHOOK = "https://webhook.site/3f45d9e8-9999-dddd-cccc-4444ee556677"

def send_alert(threat_level, detected_objects):
    latitude, longitude = get_location()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    alert_msg = {
        "threat_level": threat_level,
        "objects_detected": detected_objects,
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "timestamp": timestamp,
        "status": "ALERT"
    }

    print(f"\n🚨 ALERT SENT 🚨")
    print(f"Threat: {threat_level}")
    print(f"Objects: {', '.join(detected_objects)}")
    print(f"Time: {timestamp}")
    print(f"Location: Latitude={latitude}, Longitude={longitude}")

    # Send alert to police (test webhook)
    try:
        police_response = requests.post(POLICE_ALERT_WEBHOOK, json=alert_msg)
        print("✔️ Police notified:", police_response.status_code)
    except Exception as e:
        print("❌ Failed to notify police:", e)

    # Send alert to owner
    try:
        owner_response = requests.post(OWNER_ALERT_WEBHOOK, json=alert_msg)
        print("✔️ Owner notified:", owner_response.status_code)
    except Exception as e:
        print("❌ Failed to notify owner:", e)

# 🔽 Example call
# send_alert("High", ["person", "knife"])
