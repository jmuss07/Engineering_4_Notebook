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