# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad Part 1](#Launchpad_Part_1)
* [Launchpad Part 2](#Launchpad_Part_2)
* [Launchpad Part 3](#Launchpad_Part_3)
* [Launchpad Part 4](#Launchpad_Part_4)
* [Crash Avoidance Part 1](#Crash_Avoidance_Part_1)
* [Crash Avoidance Part 2](#Crash_Avoidance_Part_2)
* [Crash Avoidance Part 3](#Crash_Avoidance_Part_3)
* [Crash Avoidance Part 4](#Crash_Avoidance_Part_4)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Launchpad_Part_1

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

I felt pretty confident on this assignment, since I've used for-loops before. However, I had to look up how to change the increment by which it counts so that it goes backwards instead of fowards, since I needed a refresher. Other than that, I feel that the assignment went pretty well!


&nbsp;

## Launchpad_Part_2

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

This assignment also went pretty well, though I definitely had to give myself a refresher on the coding for the LEDs, especially when combining them with the for-loop. I also needed to take some time to get used to wiring things to the Pico, since the pin system/arrangement/setup is much different than that of a Metro or Uno.

&nbsp;


## Launchpad_Part_3

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

Because of the way the Pico sends signals to the button, as opposed to the Metro, I had to get used to the new system. On the bright side, I didn't have to use any resistors! I did have to make sure I used "Pull.UP" instead of "Pull.DOWN", since that would change the wiring needed for the pushbutton.

&nbsp;


## Launchpad_Part_4

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


## Crash_Avoidance_Part_1

### Assignment Description

The goal of this assignment was to code an accelerometer to continuously print the values of acceleration in the x, y, and z directions to the serial monitor. 

### Evidence

The code in action!

!(The code in action!)[]

### Wiring



### Code
Here's [the code!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance/crash_avoidance_part_one.py)
``` py
import board
import adafruit_mpu6050
import busio
import time

sda_pin = board.GP16 #sets pin for sda
scl_pin = board.GP17 #sets pin for scl
i2c = busio.I2C(scl_pin, sda_pin) #sets i2c
mpu = adafruit_mpu6050.MPU6050(i2c) #initiates accelerometer

print("code running!") #visual confirmation that code is running!

while True:
    print(mpu.acceleration) #print values of acceleration
    time.sleep(1) #wait one second
```

### Reflection
I found this assignment tricky. I've never worked with an accelerometer before, so I had to learn how to work one. Once I got it figured out, it seemed to go pretty well though!


&nbsp;


## Crash_Avoidance_Part_2

### Assignment Description



### Evidence



### Wiring



### Code


### Reflection



&nbsp;


## Crash_Avoidance_Part_3

### Assignment Description



### Evidence



### Wiring



### Code


### Reflection



&nbsp;


## Crash_Avoidance_Part_4

### Assignment Description



### Evidence



### Wiring



### Code


### Reflection





## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Here's a test link!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/raspberry-pi/test.py)
### Test Image
![Some battle droids for you!](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/guess%20im%20the%20commander%20now.jpg?raw=true)
### Test GIF
![Actually, on second thought, here's some more](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/droids.gif?raw=true)
