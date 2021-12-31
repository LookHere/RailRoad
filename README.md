# RailRoad
### Model Railroad Controller

Input GPIO 4 = LED button

Input GPIO 6 = chicken button

Out GPIO 24 = candle LED

Out GPIO 18 = servo 1 (Continuous rotation)

Out GPIO 9 = servo 2 (position based)

### How it works
Utilizes [raspberry-gpio-python](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/) to access the GPIO pins.


### Wiring diagram
![](https://raw.githubusercontent.com/LookHere/RailRoad/master/images/diagram-1b.png)
(See https://www.digikey.com/en/maker/blogs/2021/how-to-control-servo-motors-with-a-raspberry-pi)


## Continuous Rotation Servo 
The first servo was the continuous rotation servo - FeeTech FS5103R.  That didn't work for the chicken movement, but could still be good for other future applications.

Unlike other servos that that rotate to a position, this servo rotates backwards or forwards:
- 1.0ms pulse - Full Speed Clockwise 
- 1.5ms pulse - Stop
- 2.0ms pulse - Full Speed Counter Clockwise 

The white (or yellow) wire is connected to GPIO 18.  The red (or orange) is connected to the 5 volt power. The black (or brown) is connected to ground.  

We set this program to a frequency of 50 hertz
Milisecond is 1,000th of a second


### Servo datasheet
https://media.digikey.com/pdf/data%20sheets/adafruit%20pdfs/154_web.pdf

### Servo coding examples
https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/

https://www.teachmemicro.com/raspberry-pi-pwm-servo-tutorial/

## Position Based Servo
The secons servo we used was a standard servo - MCM Electronics TowerPro SG-5.  

This servo used pulses to move to specific locations
- 1.0ms pulse - Full Left, -90 degree position  
- 1.5ms pulse - Middle, 0 degree position 
- 2.0ms pulse - Full Right, 90 degree position 

The orange wire is connected to GPIO 9.  The brown is connected to ground.  The yellow is connected to the 5 volt power.  ????


### Servo datasheet

### Servoc coding examples
https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep


## Lighting
To get the lights to flicker on their own, we're using "Evil Mad Science Candle Flicker LED Assortment"

The long side for LED connects to the positive (red wire), then to a 220 Ohm Resistor, and then to GPIO 24.  The short side connects to the ground (green wire).
