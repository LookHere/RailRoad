import time
import datetime
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)

# Callback functions that execute when GPIO values change:
def button_led(channel):
    #
    # Detects LED button press
    #
    print("LED button pressed!")
    # Set the LED to be opposite its current value:
    GPIO.output(24, not GPIO.input(24))

def button_chicken(channel):
    #
    # Detects chicken button press
    #
    print("Chicken button pressed!")

# Define the GPIO pins we'll be using:
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(4, GPIO.RISING, callback=button_led, bouncetime=200)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.RISING, callback=button_chicken, bouncetime=200)

GPIO.setup(24, GPIO.OUT)

# Set the initial output values
GPIO.output(24, GPIO.HIGH)

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("Interrupted!")
    GPIO.cleanup()
