#type:ignore
import board
import time

def triangle_area(list_1, list_2, list_3): #creates function
    try:
        Ax = float(list_1[0]) #converts the first value in the first coordinate pair from a string to a useable number 
        Ay = float(list_1[1]) #converts the second value in the first coordinate pair from a string to a useable number
        Bx= float(list_2[0])#converts the first value in the second coordinate pair from a string to a useable number
        By = float(list_2[1])#converts the second value in the second coordinate pair from a string to a useable number
        Cx = float(list_3[0])#converts the first value in the third coordinate pair from a string to a useable number
        Cy = float(list_3[1])#converts the second value in the third coordinate pair from a string to a useable number
        area = abs(Ax*(By-Cy) + Bx*(Cy - Ay) + Cx*(Ay - By))/2 #do the math for the area of a triangle
        print(f"\nThe area of the triangle with vertices ({Ax},{Ay}), ({Bx},{By}), ({Cx},{Cy}) is {area} square km!")
        return area
    except: #if there are any errors do this
        print("\nSorry, these points do not form a valid triangle. Please try again, and make sure you are using the x,y sintax!")
                

cont = False #creates a variable and sets it to False
while not cont:
    start = input("\nType 'start' to begin, or type -q to quit: ").lower() #prints a question to the REPL, then sets the variable "start" to the lowercase version of the user input
    if start == "-q": #if "-q" is input
        cont = True #breaks the loop
    else:
        coord_1 = input("\nInput first coordinate in format x,y: ") #asks a question, then takes user input
        list_1 = coord_1.split(",") #splits up the last input at the comma, and sets it equal to a new variable

        coord_2 = input("\nInput second coordinate in format x,y: ") #asks a question, then takes user input
        list_2 = coord_2.split(",") #splits up the last input at the comma, and sets it equal to a new variable

        coord_3 = input("\nInput third coordinate in format x,y: ") #asks a question, then takes user input
        list_3 = coord_3.split(",")  #splits up the last input at the comma, and sets it equal to a new variable
        triangle_area(list_1, list_2, list_3) #calls/uses the function created at the start of the code