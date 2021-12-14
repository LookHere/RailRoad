# RailRoad
### Model Railroad Controller

Input GPIO 4 = LED button

Input GPIO 6 = chicken button

Out GPIO 24 = candle LED

Out GPIO 18 = servo 1

Out GPIO ?? = servo 2

### How it works
Utilizes [raspberry-gpio-python](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/) to access the GPIO pins.


### Wiring diagram
![](https://raw.githubusercontent.com/LookHere/RailRoad/master/images/diagram-1b.png)
(See https://www.digikey.com/en/maker/blogs/2021/how-to-control-servo-motors-with-a-raspberry-pi)


##Servo 

Continuous Rotation Servo - FeeTech FS5103R

Unlike other servos that that rotate to a position, this servo rotates backwards or forwards 

- Clockwise - "0" (1ms pulse)
- Stop - position "90" (1.5ms pulse)
- Counter Clockwise - position "180" (2ms pulse)

Set to frequency of 50 herts
Milisecond is 1,000th of a second



### Servo datasheet
https://media.digikey.com/pdf/data%20sheets/adafruit%20pdfs/154_web.pdf

### Servo coding examples
https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/

https://www.teachmemicro.com/raspberry-pi-pwm-servo-tutorial/
