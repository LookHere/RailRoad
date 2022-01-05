import time
import datetime
import RPi.GPIO as GPIO
import os
from pydub import AudioSegment
from pydub.playback import play

#song = AudioSegment.from_wav("sound.wav")
#play(song)

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
    play(AudioSegment.from_wav("chicken2.wav"))
    chicken_move()

def chicken_move():
    global p

#SetAngle method of movement
#    SetAngle(50)
#    SetAngle(22)
#    SetAngle(100,0.5)

#SetServoPercent method of movment
#    zero is full reverse
#    50 is stop
#    100 is full forward
    """
    SetServoPercent(50,1) #come out
    print("chicken comes out")
    #SetServoPercent(40,2) #pause

   # for x in range(10):
   #      SetServoPercent(30,0.5) #jimmy back
   #      SetServoPercent(50,0.5) #jimmy forward
   #      print("jimmy")

    SetServoPercent(30,1)  #back home
    print("chicken goes back")


    print("Chicken movement done!") 
    """

#Position based movement
    print("chicken start")
    p.ChangeDutyCycle(2.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(1.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(3.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(1.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(3.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(1.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(3.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(12.5)
    print("chicken end")


#code for position servo
def SetAngle(angle, dur=1):
    duty = angle / 18 + 2
    GPIO.output(9, True)
    p.ChangeDutyCycle(duty)
    time.sleep(dur)
    GPIO.output(9, False)
    p.ChangeDutyCycle(0)

#code for continuing servo
def SetServo(duty, dur=1):
    GPIO.output(9, True)
    p.ChangeDutyCycle(duty)
    time.sleep(dur)
    GPIO.output(9, False)
    p.ChangeDutyCycle(0)


#code for position servo that is scaled up
def SetServoPercent(duty, dur=2):
    scaler = make_interpolater(0, 100, 5, 10)
    GPIO.output(9, True)
    print("scaler {} ".format(scaler(duty)))
    p.ChangeDutyCycle(scaler(duty))
    time.sleep(dur)
    GPIO.output(9, False)
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





"""

servoPIN = 9
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 9 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
"""


# Define the GPIO pins we'll be using:

# LED Input:
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(4, GPIO.RISING, callback=button_led, bouncetime=200)

# Chicken Input:
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.RISING, callback=button_chicken, bouncetime=200)

# LED  Output:
GPIO.setup(24, GPIO.OUT)

# Chicken Output:
GPIO.setup(9, GPIO.OUT)

# Set the initial output values
GPIO.output(24, GPIO.HIGH)
p = GPIO.PWM(9, 50)
p.start(0)

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("Interrupted!")
    p.stop()
    GPIO.cleanup()
