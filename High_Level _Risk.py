import time 
import serial 
import board 
import busio 
import joblib 
import requests 
import adafruit_ads1x15.ads1115 as ADS 
from adafruit_ads1x15.analog_in import AnalogIn 
import numpy as np 
import RPi.GPIO as GPIO 
 
# Suppress warnings for clean output 
import warnings 
warnings.filterwarnings("ignore", category=UserWarning) 
 
# GPIO setup 
GPIO.setmode(GPIO.BCM) 
BUZZER = 9 
MOTOR = 8 
GPIO.setup(BUZZER, GPIO.OUT) 
GPIO.setup(MOTOR, GPIO.OUT) 
 
# ADS1115 for alcohol sensor 
Page 41 of 49 
 
i2c = busio.I2C(board.SCL, board.SDA) 
ads = ADS.ADS1115(i2c) 
chan = AnalogIn(ads, ADS.P0) 
 
# Load ML model and scaler 
model = joblib.load("/home/pi/Desktop/codes/theft_model.pkl") 
scaler = joblib.load("/home/pi/Desktop/codes/scaler.pkl") 
 
# ThingSpeak config 
THINGSPEAK_API_KEY = "LNKZVVBN4IK15IWW" 
THINGSPEAK_URL = "https://api.thingspeak.com/update" 
 
# Serial for GPS (NEO-6M) 
gps_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1) 
 
# Simulated AI bot police alert 
def alert_police(location, level): 
    print(f"[AI Bot Alert] Threat Level: {level}, Location: {location}") 
    print("Police Alert Sent Successfully (Simulated)") 
 
def get_gps_location(): 
    try: 
        line = gps_serial.readline().decode("utf-8", errors="ignore") 
        if "$GPGGA" in line: 
            data = line.split(",") 
            if data[2] and data[4]:  # Latitude and Longitude 
                lat = float(data[2]) / 100 
                lon = float(data[4]) / 100 
Page 42 of 49 
 
                return f"{lat:.4f}, {lon:.4f}" 
        return "Location Unavailable" 
    except Exception: 
        return "GPS Error" 
 
# ML classification function 
def classify_threat(voltage): 
    scaled = scaler.transform([[voltage]]) 
    prediction = model.predict(scaled)[0] 
    if prediction == 2: 
        return "High Risk" 
    elif prediction == 1: 
        return "Medium Risk" 
    else: 
        return "Low Risk" 
 
# Actuator controls 
def buzz(on=True): 
    GPIO.output(BUZZER, GPIO.HIGH if on else GPIO.LOW) 
 
def motor(on=True): 
    GPIO.output(MOTOR, GPIO.LOW if on else GPIO.HIGH) 
 
# Send data to ThingSpeak 
def log_data(voltage, level): 
    payload = { 
        "api_key": THINGSPEAK_API_KEY, 
        "field1": voltage, 
Page 43 of 49 
 
        "field2": level 
    } 
    try: 
        requests.get(THINGSPEAK_URL, params=payload) 
        print("Logged to ThingSpeak.") 
    except: 
        print("ThingSpeak logging failed.") 
 
# Main loop simulation 
try: 
    print("Theft Sentry Active") 
    while True: 
        voltage = chan.voltage 
        level = classify_threat(voltage) 
        location = get_gps_location() 
 
        print(f"Voltage: {voltage:.2f}V | Risk: {level} | Location: {location}") 
 
        # Response logic 
        if level == "High Risk": 
            buzz(True) 
            motor(False) 
            alert_police(location, level) 
        elif level == "Medium Risk": 
            buzz(True) 
            motor(True) 
        else: 
            buzz(False) 
Page 44 of 49 
 
            motor(True) 
 
        log_data(voltage, level) 
        time.sleep(5) 
 
except KeyboardInterrupt: 
    print("System Interrupted. Cleaning up...") 
    GPIO.cleanup()
