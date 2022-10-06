import board
import time
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
displayio.release_displays() #set up for OLED screen

sda_pin = board.GP16 #sets pin for sda
scl_pin = board.GP17 #sets pin for scl
i2c = busio.I2C(scl_pin, sda_pin) #sets i2c

display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP2) #sets up OLED screen
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) #sets up OLED screen

    
max_area = 100  
mid_x = 64 #x-coordinate of center of OLED screen display
mid_y = 32 #y-coordinate of center of OLED screen display
min_distance = 10000000000

def triangle_area(Ax, Ay, Bx, By, Cx, Cy): #creates function
        area = abs(Ax*(By-Cy) + Bx*(Cy - Ay) + Cx*(Ay - By))/2 #do the math for the area of a triangle
        
        Ox = round((Ax+Bx+Cx)/3, 2) #finds x-coordinate of centroid
        Oy = round((Ay+By+Cy)/3, 2) #finds y-coordinate of centroid
        
        splash = displayio.Group() #creates display group
        
        print(area)
        print(f"{Ox}, {Oy}")
        
        distance = round((((mid_x-Ox)**2)+((mid_y-Oy)**2))**1/2, 2) #solves for the distance from the centroid to the origin
        
        hline = Line(0,32,128,32, color=0xFFFF00) #sets color, start coordinates, and end coordinates of the line serving as the x-axis
        splash.append(hline) #adds to splash
        
        vline = Line(64,64,64,0, color=0xFFFF00) #sets color, start coordinates, and end coordinates of the line serving as the y-axis
        splash.append(vline) #adds to splash
        
        triangle = Triangle(int(Ax+64), int(-Ay+32), int(Bx+64), int(-By+32), int(Cx+64), int(-Cy+32), outline=0xFFFF00) #sets color and coordinates for vertices of a triangle
        splash.append(triangle)#adds to splash
        
        title = f"Area: {area}" #adds text with area of triangle to display group
        text_area = label.Label(terminalio.FONT, text = title, color = 0xFFFF00, x = 5, y= 5) #sets font, text, color, and location
        splash.append(text_area) #adds to splashs
        
        title = f"Distance: {distance}" #adds text with distance from centroid to origin to display group
        text_area = label.Label(terminalio.FONT, text = title, color = 0xFFFF00, x = 5, y= 15) #sets font, text, color, and location
        splash.append(text_area) #adds to splashs

        display.show(splash) #sends display group to OLED screen
        
        return [area, distance]
           
points = [[-50,-17,-57,12,-22,-7],[28,-14,60,-7,54,18],[45,30,51,-1,18,6],[5,5,19,15,22,10]] #List of all points used, each set of inner brackets contains the coordinates for one full triangle
for i in range(len(points)): #loops it so that it does this process for every set of coordinates ("len(points)" refers to how many lists are in "points")
    Ax = points[i][0] #sets Ax to the first number in the list
    Ay = points[i][1] #sets Ay to the second number in the list
    Bx = points[i][2] #sets Bx to the third number in the list
    By = points[i][3] #sets Vy to the fourth number in the list
    Cx = points[i][4] #sets Cx to the fifth number in the list
    Cy = points[i][5] #sets Cy to the sixth number in the list
    data = triangle_area(Ax, Ay, Bx, By, Cx, Cy) #calls/uses the function created at the start of the code
    if data[0] > max_area and data[1] < min_distance: 
        max_area = data[0] #replace the current max_area with the area of the new triangle
        min_distance = data[1] #replaces the current min_distance with the distance of the new triangle
        Ax_max = Ax
        Ay_max = Ay
        Bx_max = Bx
        By_max = By
        Cx_max = Cy
        Cy_max = Cy
    time.sleep(1)
print(f"The closest suitable landing area has vertices ({Ax_max}, {Ay_max}), ({Bx_max}, {By_max}), ({Cx_max}, {Cy_max}). The area is {max_area} km2 and the centroid is {min_distance} km away from base.")