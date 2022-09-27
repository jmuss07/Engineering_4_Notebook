import board
import time

cont = False
while not cont:
    start = input("\nType 'start' to begin, or type -q to quit: ").lower()
    if start == "-q":
        cont = True
    else:
        coord_1 = input("\nInput first coordinate in format x,y: ")
        list_1 = coord_1.split(",")
        float(list_1[0])
        float(list_1[1])
        coord_2 = input("\nInput second coordinate in format x,y: ")
        list_2 = coord_2.split(",")
        float(list_2[0])
        float(list_2[1])
        coord_3 = input("\nInput third coordinate in format x,y: ")
        list_3 = coord_3.split(",")
   
   
        
'''
        = input(f"\nIs '{phrase}' correct? (Y/N)\t")
        if confirm.lower() == "y":
            print()
            for i in phrase:
                print(i)
                if i not in asl_dict:
                    print(f"Sorry, I don't know how to sign {i}")
                else:
                    asl_dict[i]()
                    time.sleep(1)
'''