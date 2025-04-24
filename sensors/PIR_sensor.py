import RPi.GPIO as GPIO
import time

PIR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def detect_motion():
    time.sleep(1)
    return GPIO.input(PIR_PIN)
