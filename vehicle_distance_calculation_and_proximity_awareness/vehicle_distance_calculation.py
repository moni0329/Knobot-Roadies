import RPi.GPIO as GPIO
import time
import pyttsx3

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins for the ultrasonic sensor
TRIG = 23
ECHO = 24

# Setup GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Initialize text-to-speech engin
engine = pyttsx3.init()

def speak(message):
    """Speak a given message using the text-to-speech engine."""
    engine.say(message)
    engine.runAndWait()

def measure_distance():
    """Measure the distance using the HC-SR04 sensor."""
    # Send a 10us pulse to TRIG
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for the echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    # Wait for the echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start

    # Distance calculation (speed of sound is approximately 34300 cm/s)
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance

try:
    while True:
        # Measure the distance
        dist = measure_distance()
        print(f"Measured Distance = {dist:.2f} cm")

        # Determine if it's safe to cross the road
        if dist >= 500:
            message = "You can cross the road safely."
        else:
            message = "You cannot cross the road safely."

        # Print and speak the message
        print(message)
        speak(message)

        # Wait for a second before measuring again
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup GPIO pins on interrupt
    print("Measurement stopped by User")
    GPIO.cleanup()