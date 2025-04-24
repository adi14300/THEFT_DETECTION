import RPi.GPIO as GPIO
import time
from twilio.rest import Client #import here so we can catch import errors.

# Replace with your actual phone number or email and messaging setup
ALERT_PHONE_NUMBER = "+917995637251"  # Example phone number
ALERT_EMAIL_ADDRESS = "adithya221181109@gmail.com"  # Example email
USE_SMS = True  # Set to False if using email

try:
    GPIO.setmode(GPIO.BCM)

    TRIG = 19
    ECHO = 13
    BUZZER = 26
    ALERT_DISTANCE = 100

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(BUZZER, GPIO.OUT)

    def send_alert_message(message):
        """Sends an alert message via SMS or email."""
        if USE_SMS:
            try:
                # Replace with your SMS sending code (e.g., using Twilio)
                account_sid = "ACa60a9aa3fbc068ca6d8a9bb103b7b9e8" #make sure these are correct.
                auth_token = "f64ba1cc0384e20ae24ce5ca0fcae695" #make sure these are correct.
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body=message,
                    from_="+17812306693",  # Your Twilio number
                    to=ALERT_PHONE_NUMBER,
                )
                print(f"SMS sent: {message.sid}")

            except ImportError:
                print("Twilio library not found. Install it: pip install twilio")
            except Exception as e:
                print(f"Error sending SMS: {e}")
        else:  # Use email
            #email code here.
            pass

    while True:
        GPIO.output(TRIG, False)
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if 2 < distance < ALERT_DISTANCE:
            print(f"Distance: {distance - 0.5} cm")
            GPIO.output(BUZZER, True)
            print("Buzzer ON")
            send_alert_message("Unauthorized object detected!")
            time.sleep(1)
        else:
            print(f"Distance: {distance - 0.5} cm")
            GPIO.output(BUZZER, False)
            print("Buzzer OFF")
            time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by User")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup() #cleanup here.
