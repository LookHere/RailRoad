# RailRoad

Many model railroad enthusiasts have basements filled with photo-realistic layouts or join clubs with amazing cities and yards. I’m not an enthusiast, but a few years ago I pulled out an old Lionel set I had as a kid and thought a new paint job could make it look less plasticy. I’ve never built a layout (nor would I have room for a large one) but occasionally I’d send a train around a loop or paint a few figures.

<img src="https://github.com/LookHere/RailRoad/blob/main/images/Logo.png" width=100% height=100%>

Although I’ve never worked with Raspberry Pi, servos, resistors or done much coding, the balena platform made it easy to get started. It also makes it easy to add and manage additional devices when I’m ready to expand my setup. Although building my first scene still took some effort, I’m happy with the final results (see video above).

## Part of the balenaLabs Residency Projects

Every new balenista starts their journey by creating a project as [part of their onboarding](https://www.balena.io/blog/balenalabs-residencies-our-quest-to-improve-onboarding-at-balena/). This project guide is my reflection of my own residency, allowing me to meet new teammates, get to know the platform, and understand how our users put balena products to work.

To learn more about this unique opportunity, see my article ["How We Craft an Entirely Different Onboarding Experience"](https://www.linkedin.com/pulse/how-we-craft-entirely-different-onboarding-experience-john-kelly?trk=public_profile_article_view).

## The Scene

I thought it would be fun to think about a specific time and location to ground the model in history. I decided the scene should be on October 31st of 1873 near the Kissena Lake stop of the [Central Railroad of Long Island](https://en.wikipedia.org/wiki/Central_Railroad_of_Long_Island).

The farming community would have celebrated Halloween largely as a festival of the harvest, coming together at large banquites. Although it only ran from 1871 to 1874, the The Central Railroad of Long Island started a transformation in the community, from rural farmland into what would eventually be part of urban New York City.

## Project overview

The center of the operation is a Raspberry Pi running balenaOS and connected to balenaCloud. That way I can flash the device once (using balenaEtcher) and then easily update the code via wifi, making changes in the cloud and never having to take out the SD card again (something that’ll be very helpful if the pi is installed in a layout).

I wanted the project to be robust, but also easy to assemble and change. I started laying out the parts on a breadboard, and then once I was satisfied with my circuit design, I soldered all the parts to a Perma-Proto PCB. That board was then connected to the Raspberry Pi GPIO pins via screw terminals on a HAT.

# Tutorial

## Hardware required

Most of the basic parts were from the CanaKit Pi 4 Ultimate Kit, which was a good way to start. Each action only needed one additional item: the chicken needed a servo, the lighting needed LEDs, and the sound needed an audio output. The only tools I needed were a soldering iron (with some wire, lead, & flux) and a screwdriver (with some screws).

- Raspberry pi 4 - [CanaKit Raspberry pi 4 2GB Ultimate Maker Kit](https://www.microcenter.com/product/611946/canakit-raspberry-pi-4-2gb-ultimate-maker-kit)
- SD card
- Screw Terminal Hat - [52Pi RPi GPIO Screw Terminal Hat](https://www.microcenter.com/product/632047/52pi-rpi-gpio-screw-terminal-hat)
- Circuit Board - [Adafruit Perma-Proto Half-sized Breadboard PCB](https://www.adafruit.com/product/571)
- Power adaptor for the circuit board - [5V 2A (2000mA) switching power supply](https://www.adafruit.com/product/276)
- Power connection - [Breadboard-friendly 2.1mm DC barrel jack](https://www.adafruit.com/product/373) ([spec sheet](https://cdn-shop.adafruit.com/datasheets/21mmdcjackDatasheet.pdf))
- Continuous Rotation Servo - [FeeTech FS5103R](https://www.adafruit.com/product/373) ([spec sheet](https://media.digikey.com/pdf/data%20sheets/adafruit%20pdfs/154_web.pdf) and [more spec sheet](https://www.pololu.com/file/0J1433/FS5106R-specs.pdf))
- Position Based Servo - [MCM Electronics TowerPro SG-5 Standard Servo](https://www.microcenter.com/product/454407/mcm-electronics-towerpro-sg-5-standard-servo)
- Speaker connection - [USB Audio Adapter](https://www.adafruit.com/product/1475)
- Lights - [Evil Mad Science Candle Flicker LED Assortment - 15 Piece](https://www.microcenter.com/product/453261/evil-mad-science-candle-flicker-led-assortment-15-piece)
- Buttons - [16mm Illuminated Pushbutton](https://www.adafruit.com/product/1439)

## Tools and materials

- Soldering Iron - [Aven Soldering Iron with Fine Tip - 40W](https://www.microcenter.com/product/442727/aven-soldering-iron-with-fine-tip-40w) (this is a [great beginner tutorial on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/tools))
- Solder 60/40 - [Rosin Core - 0.5mm/0.02" diameter - 50 grams](https://www.adafruit.com/product/1886)
- Connections (to easily plug in servos and lights) - [Extra-long break-away 0.1" 16-pin strip male header (5 pieces)](https://www.adafruit.com/product/400)
- Wire - [Hook-up Wire Spool](https://www.adafruit.com/product/1311)
- Screwdriver and screws
- Speakers to play the audio output

## Software required

- You’ll need a [balenaCloud account](https://dashboard.balena-cloud.com/signup) – remember: your first ten devices are free and fully-featured!
- The code for this project is available [on balenaHub](https://hub.balena.io/organizations/johnkellyiv/projects/RailRoad)
- Use a tool like [Etcher](https://www.balena.io/etcher/) to flash the OS image onto your SD card
- You can also [download balenaCLI](https://github.com/balena-io/balena-cli) if you want to get into the nitty-gritty of device management via command line

# Assembly
My project looks very specific to my individual use case, but I mainly want to show how someone can start automating motors and LEDs with balena. You can take this in any direction you want, or just replicate your own version of what I’ve built.
It all starts with creating your balenaCloud account and clicking this button to add this project as a Fleet within your dashboard:

[Deploy with balena](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/LookHere/RailRoad)

The entire project was written in python and can be found [here on GitHub](https://github.com/LookHere/RailRoad/tree/main/controller). The docker-compose.yml sets up the different containers. 



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

To wire the servo: 
- The white (or yellow) wire is connected to the signal.  
- The red (or orange) is connected to the 5 volt power. 
- The black (or brown) is connected to ground.  

We set this program to a frequency of 50 hertz.
Milisecond is 1,000th of a second.

## Continuous Rotation Servo 
The first servo was the continuous rotation servo - FeeTech FS5103R.  That didn't work for the chicken movement, but could still be good for other future applications.

Unlike other servos that that rotate to a position, this servo rotates backwards or forwards:
- 1.0ms pulse - Full Speed Clockwise 
- 1.5ms pulse - Stop
- 2.0ms pulse - Full Speed Counter Clockwise
 
For this servo, we used GPIO 18 to control the movement.

### Servo datasheet
https://media.digikey.com/pdf/data%20sheets/adafruit%20pdfs/154_web.pdf

### Servo coding examples
https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/

https://www.teachmemicro.com/raspberry-pi-pwm-servo-tutorial/

## Position Based Servo
The second servo we used was a standard servo - MCM Electronics TowerPro SG-5.  

This servo used pulses to move to specific locations
- 1.0ms pulse - Full Left, -90 degree position  
- 1.5ms pulse - Middle, 0 degree position 
- 2.0ms pulse - Full Right, 90 degree position 

For this servo, we used GPIO 9 (also known as miso) to control the movement.

### Servo datasheet

### Servoc coding examples
https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep


## Lighting
To get the lights to flicker on their own, we're using "Evil Mad Science Candle Flicker LED Assortment"

The long side for LED connects to the positive (red wire), then to a 220 Ohm Resistor, and then to GPIO 24.  The short side connects to the ground (green wire).
