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

#    SetAngle()
#    SetAngle(22)
#    SetAngle(100,0.5)

    #zero is full reverse
    SetServoPercent(1) 

    #50 is stop
    SetServoPercent(50)

    #100 is full forward
    SetServoPercent(99)


    print("Chicken movement done!")

#code for position servo
def SetAngle(angle, dur=1):
    duty = angle / 18 + 2
    GPIO.output(18, True)
    p.ChangeDutyCycle(duty)
    time.sleep(dur)
    GPIO.output(18, False)
    p.ChangeDutyCycle(0)

#code for continuing servo
def SetServo(duty, dur=1):
    GPIO.output(18, True)
    p.ChangeDutyCycle(duty)
    time.sleep(dur)
    GPIO.output(18, False)
    p.ChangeDutyCycle(0)


#code for position servo that is scaled up
def SetServoPercent(duty, dur=2):
    scaler = make_interpolater(0, 100, 5, 10)
    GPIO.output(18, True)
    print("scaler {} ".format(scaler(duty)))
    p.ChangeDutyCycle(scaler(duty))
    time.sleep(dur)
    GPIO.output(18, False)
    p.ChangeDutyCycle(0)


def make_interpolater(left_min, left_max, right_min, right_max):
    #
    # Scales one range to another...
    # Function that returns a function (closure)
    # see https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
    #

    # Figure out how 'wide' each range is  
    leftSpan = left_max - left_min  
    rightSpan = right_max - right_min  

    # Compute the scale factor between left and right values 
    scaleFactor = float(rightSpan) / float(leftSpan) 

    # create interpolation function using pre-calculated scaleFactor
    def interp_fn(value):
        return right_min + (value-left_min)*scaleFactor

    return interp_fn

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
p = GPIO.PWM(18, 50)
p.start(0)

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Interrupted!")
    p.stop()
    GPIO.cleanup()
