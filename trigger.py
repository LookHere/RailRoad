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
    chicken_move()

def chicken_move():
    global p

    p.start(5) # Initialization

    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(11.5) # may need to be adjusted
    time.sleep(1)
    p.ChangeDutyCycle(20.5)
    time.sleep(1)
    p.ChangeDutyCycle(11.5) # may need to be adjusted
    print("Chicken movement done!")

# Define the GPIO pins we'll be using:
# Inputs:
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(4, GPIO.RISING, callback=button_led, bouncetime=200)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.RISING, callback=button_chicken, bouncetime=200)

# Outputs:
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# Set the initial output values
GPIO.output(24, GPIO.HIGH)
p = GPIO.PWM(18, 100)

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Interrupted!")
    GPIO.cleanup()
