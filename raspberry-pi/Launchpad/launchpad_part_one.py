import board
import time

for i in range(10, -1, -1): #creates a range of numbers from 10 to -1, but does not inbclude -1 in the list; also indicates that we're counting down by 1
    if i == 0: #only runs if the value of the counter is 0
        print("Liftoff!") #prints "Liftoff!"
    else: #runs if the counter is at any other value in the range
        print(i) #prints the current value of the counter
        time.sleep(1) #waites for 1 second before repeating