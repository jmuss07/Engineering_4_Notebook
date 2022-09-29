import board
import time

def triangle_area(list_1, list_2, list_3):
    try:
        Ax = float(list_1[0])
        Ay = float(list_1[1])
        Bx= float(list_2[0])
        By = float(list_2[1])
        Cx = float(list_3[0])
        Cy = float(list_3[1])
        area = abs(Ax*(By-Cy) + Bx*(Cy - Ay) + Cx*(Ay - By))/2
        print(f"\nThe area of the triangle with vertices ({Ax},{Ay}), ({Bx},{By}), ({Cx},{Cy}) is {area} square km!")
        return area
    except:
        print("\nSorry, these points do not form a valid triangle. Please try again, and make sure you are using the x,y sintax!")
                

cont = False
while not cont:
    start = input("\nType 'start' to begin, or type -q to quit: ").lower()
    if start == "-q":
        cont = True
    else:
        coord_1 = input("\nInput first coordinate in format x,y: ")
        list_1 = coord_1.split(",")

        coord_2 = input("\nInput second coordinate in format x,y: ")
        list_2 = coord_2.split(",")

        coord_3 = input("\nInput third coordinate in format x,y: ")
        list_3 = coord_3.split(",")
        triangle_area(list_1, list_2, list_3)