#type:ignore
import board
import time
import digitalio

red = digitalio.DigitalInOut(board.GP14) #sets pin to connect red LED to board
red.direction = digitalio.Direction.OUTPUT #sets pin type
green = digitalio.DigitalInOut(board.GP15) #sets pin to connect green LED to board
green.direction = digitalio.Direction.OUTPUT #sets pin type
button = digitalio.DigitalInOut(board.GP16) #sets pin to connect button to board
button.pull = digitalio.Pull.UP 

print("code running!")
state = "waiting"
while True:
    if state == "waiting":
        red.value = False
        green.value = False
        if button.value == False: #if button is pressed...
            state = "countdown"
    if state == "countdown":
        for i in range(10, 0, -1): #creates a range of numbers from 10 to 0, but does not include 0 in the list; also indicates that we're counting down by 1
            red.value = True #turns red LED o
            green.value = False #turns green LED off
            print(i) #prints the current value of the counter
            red.value = False #turns red LED off
            time.sleep(1) #waites for 1 second before repeating
            if button.value == False:
                state = "abort"
                break
        print("Liftoff!") #prints the phrase "Liftoff!" one second after we exit the range of numbers in the for-loop
        green.value = True #turns green LED on
    if state == "abort":
        print("ABORT!!!")
        red.value = False
        green.value = False
        state = "waiting"
        time.sleep(1)