import time 
import datetime 
import RPi.GPIO as GPIO 
import os

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(4, GPIO.RISING, callback=button_led, bouncetime=200)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.RISING, callback=button_chicken, bouncetime=200)

GPIO.setup(24, GPIO.OUT)

def button_led(channel):
    #
    # 
    #
    
    print("LED button pressed!")
    
def button_chicken(channel):
    #
    # 
    #
    
    print("Chicken button pressed!")
