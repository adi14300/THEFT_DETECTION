# Theft Sentry - High Level Security System 🚨

A smart theft detection mechanism built using Raspberry Pi, combining motion sensing, GPS tracking, AI threat classification, camera feed, and real-time alerts.

## 🔧 Components Used
- Raspberry Pi 4
- PIR Sensor
- Buzzer
- PiCamera
- NEO-6M GPS Module
- AI model (joblib)
- Python 3

## 📂 Folder Structure
- `main.py` - Main script
- `sensors/` - PIR sensor, GPS, buzzer
- `camera/` - Live video stream
- `ai_threat_classifier/` - AI-based threat detection
- `alerts/` - Alert generation (location + threat level)

## 🧠 AI Integration
The AI model classifies threats as:
- Low
- Medium
- High

## 📡 Future Enhancements
- Telegram or WhatsApp alert bot
- Cloud storage of evidence
- Advanced AI training

## 👥 Contributors
- M. Adithya (22B91A4733)
- Ch. Chandu (22B91A4709)
- D. Manoj Kumar (22B91A4715)
- P. Rakshitha (22B91A4737)

Guided by **Mr.V.S.R.K.Raju , Ms.K.Neelima**, CSE Dept, SRKR Engineering College

## 🧪 Run the Code
```bash
python3 main.py
