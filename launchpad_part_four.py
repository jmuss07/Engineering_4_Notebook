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

while True:
    if button.value == False: #if button is pressed...
        for i in range(10, 0, -1): #creates a range of numbers from 10 to 0, but does not include 0 in the list; also indicates that we're counting down by 1
            red.value = True #turns red LED on
            green.value = False #turns green LED off
            print(i) #prints the current value of the counter
            red.value = False #turns red LED off
            time.sleep(1) #waites for 1 second before repeating
        print("Liftoff!") #prints the phrase "Liftoff!" one second after we exit the range of numbers in the for-loop
        while True:
            green.value = True #turns green LED on #
            