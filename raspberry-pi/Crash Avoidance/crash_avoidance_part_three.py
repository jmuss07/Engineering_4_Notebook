#type:ignore
import board
import adafruit_mpu6050
import busio
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
displayio.release_displays() #set up for OLED screen

warning = digitalio.DigitalInOut(board.GP15) #sets pin for warning LED
warning.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP16 #sets pin for sda
scl_pin = board.GP17 #sets pin for scl
i2c = busio.I2C(scl_pin, sda_pin) #sets i2c

display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP2) #sets up OLED screen
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) #sets up OLED screen
mpu = adafruit_mpu6050.MPU6050(i2c, address = 0x68)#initiates accelerometer


print("code running!") #visual confirmation that code is running!

while True:
    splash = displayio.Group() #creates display group

    title = "ANGULAR VELOCITY" #adds title block to display group
    text_area = label.Label(terminalio.FONT, text = title, color = 0xFFFF00, x = 5, y= 5) #sets font, text, color, and location
    splash.append(text_area) #adds to splash

    x_val = f"x: {round(mpu.acceleration[0], 3)}" #adds x value text block to display group and rounds it to 3 decimal places
    text_area = label.Label(terminalio.FONT, text = x_val, color = 0xFFFF00, x = 5, y = 16) #sets font, text, color, and location
    splash.append(text_area) #adds to splash

    y_val = f"y: {round(mpu.acceleration[1], 3)}" #adds y value text block to display group and rounds it to 3 decimal places
    text_area = label.Label(terminalio.FONT, text = y_val, color = 0xFFFF00, x = 5, y= 26) #sets font, text, color, and poition
    splash.append(text_area) #adds to splash

    z_val = f"z: {round(mpu.acceleration[2], 3)}" #adds z value text block to display group and rounds it to 3 decimal places
    text_area = label.Label(terminalio.FONT, text = z_val, color = 0xFFFF00, x = 5, y= 36) #sets font, text, color, and position
    splash.append(text_area) #adds to splash
    
    display.show(splash) #sends display group to OLED screen
    print(mpu.acceleration) #print values of acceleration
    time.sleep(1) #wait one second
    
    if mpu.acceleration[0] < -9 or mpu.acceleration[0] > 9: #only do this if the x-value is >9 or <-9
         warning.value = True #turn warning LED on
    elif mpu.acceleration[1] < -9 or mpu.acceleration[1] > 9: #only do this if the y-value is >9 or <-9
         warning.value = True #turn warning LED on
    else:
        warning.value = False #turn warning LED off