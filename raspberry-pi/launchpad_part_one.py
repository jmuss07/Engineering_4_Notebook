import board
import time

for i in range(10, -1, -1):
    if i == 0:
        print("Liftoff!")
    else:
        print(i)
        time.sleep(1)