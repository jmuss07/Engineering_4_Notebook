# Engineering_4_Notebook

&nbsp;

## Table of Contents
### Code
* [Launchpad Part 1](#Launchpad-Part-1)
* [Launchpad Part 2](#Launchpad-Part-2)
* [Launchpad Part 3](#Launchpad-Part-3)
* [Launchpad Part 4](#Launchpad-Part-4)
* [Crash Avoidance Part 1](#Crash-Avoidance-Part-1)
* [Crash Avoidance Part 2](#Crash-Avoidance-Part-2)
* [Crash Avoidance Part 3](#Crash-Avoidance-Part-3)
* [Crash Avoidance Part 4](#Crash-Avoidance-Part-4)
* [Landing Area Part 1](#Landing-Area-Part-1)
* [Landing Area Part 2](#Landing-Area-Part-2)
* [Landing Area Part 3](#Landing-Area-Part-3)
* [Morse Code Part 1](#Morse-Code-Part-1)
* [Morse Code Part 2](#Morse-Code-Part-2)
### Onshape
* [FEA Part 1 (Beam Design)](#FEA-Part-1-Beam-Design)
* [FEA Part 2 (Simscale Workflow)](#FEA-Part-2-Simscale-Workflow)
* [FEA Part 3 (Iterative Design)](#FEA-Part-3-Iterative-Design)
* [Ring and Spinner](#Ring-and-Spinner)
* [Key and Prop](#Key-and-Prop)
* [Assembling the Launcher](#Assembling-the-Launcher)


&nbsp;

## Launchpad Part 1

### Assignment Description

The goal of this assignment was to create a countdown timer that goes down from 10 to 0. The value is meant to decrease by 1 every second. 

### Evidence 
The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/launchpadpt1.gif?raw=true)

### Wiring

No wiring for this assignment! 

### Code
Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad/launchpad_part_one.py) 
```python
import board
import time

for i in range(10, -1, -1): #creates a range of numbers from 10 to -1, but does not inbclude -1 in the list; also indicates that we're counting down by 1
    if i == 0: #only runs if the value of the counter is 0
        print("Liftoff!") #prints "Liftoff!"
    else: #runs if the counter is at any other value in the range
        print(i) #prints the current value of the counter
        time.sleep(1) #waites for 1 second before repeating
```

### Reflection

I felt pretty confident on this assignment, since I've used ```for``` loops before. However, I had to look up how to change the increment by which it counts so that it goes backwards instead of fowards, since I needed a refresher. To do this, you need to specify a range, with the first number being the start value, the second being the end, and the third being the increment by which it increases. By setting the third value to -1, I got it to count down by 1. It's also important to note that although the start value is included in the range, the end value is not, so you have to set it to 1 lower than what you actually want it to go to. Other than that, I feel that the assignment went pretty well!


&nbsp;

## Launchpad Part 2

### Assignment Description

The goal of this assignment was to combine the countdown timer created in the previous part with two LEDs: one that flashes red every second until liftoff, and the a green one that turns on and remains on once the countdown reaches liftoff.

### Evidence
The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/launchpad-pt-2.gif?raw=true)

### Wiring
The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/launchpad-pt2-wiring.png?raw=true)

### Code
Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad/launchpad_part_two.py)
```python
import board
import time
import digitalio

red = digitalio.DigitalInOut(board.GP14) #sets pin to connect red LED to board
red.direction = digitalio.Direction.OUTPUT #sets pin type
green = digitalio.DigitalInOut(board.GP15) #sets pin to connect green LED to board
green.direction = digitalio.Direction.OUTPUT #sets pin type

for i in range(10, 0, -1): #creates a range of numbers from 10 to 0, but does not include 0 in the list; also indicates that we're counting down by 1
  red.value = True #turns red LED on
  green.value = False #turns green LED off
  print(i) #prints the current value of the counter
  red.value = False #turns red LED off
  time.sleep(1) #waites for 1 second before repeating
print("Liftoff!") #prints the phrase "Liftoff!" one second after we exit the range of numbers in the for-loop
while True:
  green.value = True #turns green LED on
  ```
### Reflection

This assignment also went pretty well, though I definitely had to give myself a refresher on the coding for the LEDs, especially when combining them with the ```for``` loop. It's important to make sure that the ```for``` loop isn't inside a ```while True``` statement, and that you turn the green LED on outside of the ```for``` loop; this piece *does* go inside a ```while True``` statement. I also needed to take some time to get used to wiring things to the Pico, since the pin system/arrangement/setup is much different than that of a Metro or Uno.

&nbsp;


## Launchpad Part 3

### Assignment Description

The goal of this assignment was to add a push button to the code in the previous part, so that it would only run once the button was pressed, and then stop, instead of looping indefinitely.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/launchpadpt3.gif?raw=true)


### Wiring

The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/launchpad%20pt3%20wiring.PNG?raw=true)


### Code
Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad/launchpad_part_three.py)
``` py
import board
import time
import digitalio

red = digitalio.DigitalInOut(board.GP14) #sets pin to connect red LED to board
red.direction = digitalio.Direction.OUTPUT #sets pin type
green = digitalio.DigitalInOut(board.GP15) #sets pin to connect green LED to board
green.direction = digitalio.Direction.OUTPUT #sets pin type
button = digitalio.DigitalInOut(board.GP16) #sets pin to connect button to board
button.pull = digitalio.Pull.UP 

while True:
    if button.value == False:
        for i in range(10, 0, -1): #creates a range of numbers from 10 to 0, but does not include 0 in the list; also indicates that we're counting down by 1
            red.value = True #turns red LED on
            green.value = False #turns green LED off
            print(i) #prints the current value of the counter
            red.value = False #turns red LED off
            time.sleep(1) #waites for 1 second before repeating
        print("Liftoff!") #prints the phrase "Liftoff!" one second after we exit the range of numbers in the for-loop
        while True:
            green.value = True #turns green LED on #         
```

### Reflection

Because of the way the Pico sends signals to the button, as opposed to the Metro, I had to get used to the new system. On the bright side, I didn't have to use any resistors! I did have to make sure I used ```Pull.UP``` instead of ```Pull.DOWN```, since that would change the wiring needed for the pushbutton.

&nbsp;


## Launchpad Part 4

### Assignment Description

The goal of this assignment was to move a servo 180 degreees once the countdown reaches 0 in order to simulate launch, and combine it with the code from the previous part. 

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/Launchpad%20pt4.gif?raw=true)


### Wiring

The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/Launchpad%20pt4%20wiring.png?raw=true)


### Code
Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Launchpad/launchpad_part_four.py)
``` py
import board
import time
import digitalio
import pwmio
from adafruit_motor import servo #imports just  servo commands from motor library

red = digitalio.DigitalInOut(board.GP14) #sets pin to connect red LED to board
red.direction = digitalio.Direction.OUTPUT #sets pin type
green = digitalio.DigitalInOut(board.GP15) #sets pin to connect green LED to board
green.direction = digitalio.Direction.OUTPUT #sets pin type
button = digitalio.DigitalInOut(board.GP16) #sets pin to connect button to board
button.pull = digitalio.Pull.UP 
pwm_servo = pwmio.PWMOut(board.GP18, duty_cycle = 2 ** 15, frequency = 50) #defines values for general pwmio servo
launch_servo = servo.Servo(pwm_servo, min_pulse = 500, max_pulse = 2500) #sets up parameters for specific servo used for launch

print("code running!")

while True:
    if button.value == False: #if button is pressed...
        for i in range(10, 0, -1): #creates a range of numbers from 10 to 0, but does not include 0 in the list; also indicates that we're counting down by 1
            launch_servo.angle = 0 #sets servo angle to 0 degrees
            red.value = True #turns red LED on
            green.value = False #turns green LED off
            print(i) #prints the current value of the counter
            red.value = False #turns red LED off
            time.sleep(1) #waites for 1 second before repeating
        print("Liftoff!") #prints the phrase "Liftoff!" one second after we exit the range of numbers in the for-loop
        green.value = True #turns green LED on
        launch_servo.angle = 180 #sets servo angle to 180 degrees
```

### Reflection

This assignment was easier for me than the pushbutton, since I worked with quite a few servos during my [project last year](https://github.com/jmuss07/Automated-Sign-Language). In addition, I just had to add one main command at the end of the code to move the servo, and one at the beginning to move it back. Because the rest of the code was not reliant on the new addition (unlike in the last part), it was much easier to execute and test. 

&nbsp;


## Crash Avoidance Part 1

### Assignment Description

The goal of this assignment was to code an accelerometer to continuously print the values of acceleration in the x, y, and z directions to the serial monitor. 

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/crashavoidancept1.gif?raw=true)

### Wiring

The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/Launchpad%20pt4%20wiring.png?raw=true)

### Code
Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/crashavoidancept1wiring.PNG?raw=true)

### Reflection
I found this assignment tricky. I've never worked with an accelerometer before, so I had to learn how to work one. Once I got it figured out, it seemed to go pretty well though! Although the set-up commands were provided in the assignment, I wanted to fully understand how they worked, so I took extra time to figure it out. Other than that, the code is fairly straightfoward; after the setup, it only consists of a ```while True``` statement containing the commands ```print(mpu.acceleration)``` and a ```time.sleep``` function.

&nbsp;


## Crash Avoidance Part 2

### Assignment Description

The goal of this assignment was to add a warning light to the previous part that turns on any time the accelerometer is tilted 90 degrees or more in any direction.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/crashavoidancept2.gif?raw=true)

### Wiring

The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/CAP2wiring.PNG?raw=true)

### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/a2ceca7ee34c4c578c48e1bfdca3d07284f9e345/raspberry-pi/Crash%20Avoidance/crash_avoidance_part_two.py)

### Reflection

This assignment was trickier, since it involved pulling information for just some situations. Due to this, I had to learn how to specify that the code was looking at just the x or just the y information.In order to do this you have to specify ```mpu.acceleration[0]``` for the x-coordinate, and ```mpu.acceleration[1]``` for the y-coordinate. The rest of the code utilized ```if``` statements that controlled the LED based on the value found by the accelerometer, so it was just one command of ```warning.value = True``` or ```warning.value = False```.

&nbsp;


## Crash Avoidance Part 3

### Assignment Description

The goal of this assignment was to take the previous two parts and print the data from the accelerometer to an OLED screen, rounding the decimal three places.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/Crashavoidancept3.gif?raw=true)

### Wiring

The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/CAP3wiring.PNG?raw=true)

### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/a2ceca7ee34c4c578c48e1bfdca3d07284f9e345/raspberry-pi/Crash%20Avoidance/crash_avoidance_part_three.py)

### Reflection

While this assignment ended up ok, I had to learn the completely new skill of communicating with the OLED screen, as well as using two different I2C devices instead of just one. In order to do this, you have to run a seperate code file, making sure to upload it onto the board itself. After changing the ```sda``` and ```scl``` pin values to all of the ones you're using, the code will print out the I2C device names! I got this bit running just fine, but in the end, the code kept spitting random error messages at me, and I had to change the pins things were plugged in to several times before it started working.

&nbsp;


## Crash Avoidance Part 4

### Assignment Description

The goal of this assignment was to add an altimeter to the previous parts, so that the warning light won't turn on if the device is more than 3 meters above its initial altitude.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/CAP4.gif?raw=true)

### Wiring

The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/CAP4_wiring.PNG?raw=true)

### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance/crash_avoidance_part_four.py)

### Reflection


This one was more challenging, since the altimeter's initial altitude is sea level. In order to combat this, I had to make it so that it used whatever altitude it read when it turned on as the initial altitude. I did this through the command ```altitude_initial = sensor.altitude```. After resetting this value, the device can measure the current height from the initial altitude!

&nbsp;


## Landing Area Part 1

### Assignment Description

The goal of this assignment was to create a program that asks for three sets of coordinates that form a triangle, which the user then inputs, and finds the area of said triangle.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP1.gif?raw=true)

### Wiring

No wiring for this assignment!

### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Landing%20Area/landing_area_part_one.py)

### Reflection

This assignment required me to refresh my knowledge on functions and user input. However, since I had used both in my [project last year](https://github.com/jmuss07/Automated-Sign-Language), it wasn't too difficult. This was my first time using the ```split``` function, which proved to be super helpful in separating the x and y coordinates in each pair!

&nbsp;


## Landing Area Part 2

### Assignment Description

The goal of this assignment was to add an OLED screen to the previous part that would graph the triangle made from the coordinates provided by the user, and display its area.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2.gif?raw=true)

### Wiring

The wiring diagram for this part!

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2wiring.PNG?raw=true)

### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Landing%20Area/landing_area_part_two.py)

### Reflection

Getting the coordinates to display on the OLED screen was tricky. This was due to the difference in the screen size and the numbers for the coordinates. Because of this, my first test triangle was appearing off-screen, and the second was in the wrong place! After trying multiple things, I found out that you have to add 64 to the x-coordinates, and 32 to the y-coordinates (after making the y-coordinates negative).

&nbsp;


## Landing Area Part 3

### Assignment Description

The goal of this assignment was to replace the user input from the last part with a pre-set list of possible coordinate sets, which the code would then run through, displaying each triangle and area to the OLED screen, before finally determining the closest triangle with an area over 100 km.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP3.gif?raw=true)

### Wiring

The wiring diagram for this part! (It's the same wiring as the last part!)

![The wiring diagram for this part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/LAP2wiring.PNG?raw=true)

### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Landing%20Area/landing_area_part_three.py)

### Reflection

This assignment was rather tricky. The first trouble I had came from trying to loop through the list of different triangles. After that, I had to figure out how to exit said loop. The answer? DO NOT USE A ```while True``` STATEMENT!!! After that, I had to figure out a way to find a triangle that fit both requirements. I settled on an ```if``` statement that only replaces the maximum area and minimum distance if the new distance is smaller than the old one, and the new area is bigger than the old.


&nbsp;


## Morse Code Part 1

### Assignment Description

The goal of this assignment was to create a parser that would take a phrase input by the user and translate it to morse code, printing the translation to the serial monitor. In addition, it had to quit the program if the user types ```-q``` instead of a phrase.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/MCP1.gif?raw=true)

### Wiring

No wiring for this assignment!

### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Morse%20Code/morse_code_part_one.py)

### Reflection

Just like the last one, this assignment required user input. This time, it utilized a parser! Since I worked with parsing in my [project last year](https://github.com/jmuss07/Automated-Sign-Language), it wasn't too difficult. However, this time I had to learn how to concatenate strings. This process adds strings together, allowing me to print the entire translated message on one line, instead of each letter on a new line.

&nbsp;

## Morse Code Part 2

### Assignment Description

The goal of this assignment was to add an LED to the previous part that would stay on or off for various times depending on the letter or type of pause/break it was meant to communicate.

### Evidence

The code in action!

![The code in action!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/MCP2.gif?raw=true)

### Wiring

No wiring for this assignment!


### Code

Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Morse%20Code/morse_code_part_two.py)

### Reflection

This assignment wasn't too bad, since it mostly just built on the previous part. However, I had some trouble getting the ```if``` statements for the blink lengths working. The trick to that is to end the original ```for```-loop that translated and printed the morse code to the serial monitor, then add a second ```for```-loop immediately after containg the ```if``` statements controlling the LED blinks. By keeping this within the statement saying that
 ```python 
if confirm.lower() == "y":
```
 the code waits for the translated blinking to finish before looping back to the original ask.

&nbsp;




## FEA Part 1 Beam Design

### Assignment Description

The goal of this assignment was to design a beam in Onshape that would maximize the weight it could support before failing. In order to make the assignment more challenging, we had a variety of restrictions, and beam failure was classified as the beam either breaking or bending more than 35mm.

### Part Link 

Here's [the part!](https://cvilleschools.onshape.com/documents/59c81db643eb421ff4169cab/w/b284f2fe0a8eaa6940be94eb/e/aecb3df057d554533ad4fef1?renderMode=0&uiState=6363ff269f09cf7adfb890d7)

### Part Image

The part itself!

![The part itself!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/FEA_Beam_1.PNG?raw=true)

### Reflection

Before starting my design, I looked into architecture designs for strong yet light-weight designs. One of the most intriguing designs utilized a lattice for the main structure of the beam. By attaching a thinner chunk to the end of the main beam, I was able to make a shelf for the eyebolt hole. I also went through and filleted any sharp corners where different parts of the attachment block met in order to reduce any potential breaking points, since sharp corners are stress concentrators and curves are not. When designing the beam as a whole, I was reminded of a honeycomb, which may be a concept used in future iterations, especially since hexagons are particularly strong shapes. 

&nbsp;



## FEA Part 2 Simscale Workflow

### Assignment Description

In this assignment, we had to put our previously designed beam into Simscale, a site that can run FEA (Finite Element Analysis). We used it to run a structural analysis on our beam in order to find the weak points and further optimize it.

### Part Link 

Here's [the part!](https://cvilleschools.onshape.com/documents/59c81db643eb421ff4169cab/w/b284f2fe0a8eaa6940be94eb/e/aecb3df057d554533ad4fef1?renderMode=0&uiState=6363ff269f09cf7adfb890d7)

### Part Image

The Simscale model!

![The Simscale model!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/onshape/FEA_Simscale_Iteration1.PNG?raw=true)

### Reflection

The end of the beam closest to where the beam connects to the block seems to be the most likely to fail, and will probably either break or bend at this point. This may be fixable by either reinforcing this point, and reducing the mass by making the beam skinnier. It also may be possible to change the orientation of the lattices, so that they're vertical instead of horizontal.
&nbsp;



## FEA Part 3 Iterative Design

### Assignment Description

In this assignment, we had to use the results from the simulation performed in the previous part to improve our design.

### Part Link 

Here's [the part!](https://cvilleschools.onshape.com/documents/59c81db643eb421ff4169cab/w/b284f2fe0a8eaa6940be94eb/e/aecb3df057d554533ad4fef1?renderMode=0&uiState=6363ff269f09cf7adfb890d7)

### Part Image

Unfortunately, Simscale was unable to properly form a mesh of the final beam, meaning that I was unable to create a simulation. 

### Reflection
In version 3 of the beam design, I added a block to the edge closest to the attachment block, and filleted the edges to create a smoother transition. This was done because in the previous version, that edge was the weakest part that was most likely to break. I also added 4 thinner extrusions that were 5mm in width spaced 25mm apart to make sure that those areas were sturdier and less likely to break.
&nbsp;



## Ring and Spinner

### Assignment Description

This was the first part of a three-part teamwork assignment in which we made a pullcopter! In this part, one of us designed the ring, which is where the copter is held, and the other made the spinner, which is the rod that the prop sits on. I made the spinner, and my partner [Johnny](https://github.com/jkrosby51) made the ring. I'll be covering the spinner here. To find out about the ring, you can check out [Johnny's repository](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/README.md).

### Part Link 

Here's [the part!](https://cvilleschools.onshape.com/documents/126c5299402389b7ee0cfbea/w/3b41693a293f15039c4e0d37/e/e149bbc1e7d2cea44b67b81e)

### Part Image

The part!

![The part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/onshape/FEA_Simscale_Iteration1.PNG?raw=true)

### Reflection

This was a good refresher on some tools that I hadn't used in a while, especially editing in context. While I've used this feature before, it hasn't played a role in any of my recent projects. It was incredibly helpful, and allowed me to create the spinner in it's own part studio based off of previous geometries from a different part studio. This was also my first time using the helix tool, which was used to create the threads on the top half of the spinner. This tool allowed me to make a path that followed the curve of the circular face. I was then able to use a sweep to remove the area created by the helix and a previously made sketch on the top face of the spinner.

&nbsp;



## Key and Prop

### Assignment Description

This is the second part in the three part teamwork assignment. If you want to see part one, you can find it [here](#Ring-and-Spinner). In this part, one of us made the key, which is pulled in order to release the copter, and the other designed the prop, which is the piece that flys/is released from the others. I made the prop, and my partner [Johnny](https://github.com/jkrosby51) made the key. I'll be covering the prop here. To find out about the key, you can check out [Johnny's repository](https://github.com/jkrosby51/Engineering_4_Notebook/blob/main/README.md).


### Part Link 

Here's [the part!](https://cvilleschools.onshape.com/documents/126c5299402389b7ee0cfbea/w/3b41693a293f15039c4e0d37/e/e149bbc1e7d2cea44b67b81e)

### Part Image

The part!

![The part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/onshape/FEA_Simscale_Iteration1.PNG?raw=true)

### Reflection

Similarly to the previous piece, this part also utilised tools that I was already familiar with. However, I did find the method used to create the blades rather interesting. The blades were created on the front plane, as opposed to a sketch face. The sketch used featured a single parallelogram, which was drawn at the appropriate angle that we wanted the blades to be at. It was then extruded up to the inner face of the outer ring of the prop, and I used a circular pattern to create more blades. While not the way I would have initially chosen to create the blades, it was extremely effective.

&nbsp;



## Assembling the Launcher

### Assignment Description



### Part Link 

Here's [the part!](https://cvilleschools.onshape.com/documents/126c5299402389b7ee0cfbea/w/3b41693a293f15039c4e0d37/e/830f431f4d70c9975bba268f)

### Part Image

The part!

![The part!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/onshape/FEA_Simscale_Iteration1.PNG?raw=true)

### Reflection

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Here's a test link!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/test.py)
### Test Image
![Some battle droids for you!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/guess%20im%20the%20commander%20now.jpg?raw=true)
### Test GIF
![Actually, on second thought, here's some more](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/droids.gif?raw=true)
