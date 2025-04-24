from sensors.pir_sensor import detect_motion
from sensors.buzzer import trigger_buzzer
from sensors.gps_tracker import get_location
from camera.live_stream import start_stream
from ai_threat_classifier.threat_detection import classify_threat
from alerts.alert_system import send_alert

def main():
    print("[SYSTEM] Theft Sentry Activated")

    if detect_motion():
        print("[SYSTEM] Motion Detected!")
        trigger_buzzer()
        start_stream()

        features = [1, 0, 0]  # Replace with actual sensor features
        threat_level = classify_threat(features)

        send_alert(threat_level)

    else:
        print("[SYSTEM] No motion detected. System monitoring...")

if __name__ == "__main__":
    main()
