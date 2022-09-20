import board
import adafruit_mpu6050
import busio
import time
import digitalio

warning = digitalio.DigitalInOut(board.GP15) #sets pin for warning LED
warning.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16 #sets pin for sda
scl_pin = board.GP17 #sets pin for scl
i2c = busio.I2C(scl_pin, sda_pin) #sets i2c
mpu = adafruit_mpu6050.MPU6050(i2c) #initiates accelerometer

print("code running!") #visual confirmation that code is running!

while True:
    print(mpu.acceleration) #print values of acceleration
    time.sleep(1) #wait one second
    if mpu.acceleration[0] < -9 or mpu.acceleration[0] > 9: #only do this if the x-value is >9 or <-9
         warning.value = True #turn warning LED on
    elif mpu.acceleration[1] < -9 or mpu.acceleration[1] > 9: #only do this if the y-value is >9 or <-9
         warning.value = True #turn warning LED on
    else:
        warning.value = False #turn warning LED off