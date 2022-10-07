import board
import time

# Morse code dictionary!
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

morse = ' ' #creates an empty string
cont = False
while not cont:
    phrase = input("\nPlease enter a phrase, or type -q to quit: ").upper() #asks for user input, and sets the input equal to 'phrase'
    if phrase == "-Q":
        cont = True #exits the code
    else:
        confirm = input(f"\nIs '{phrase}' correct? (Y/N)\t") #asks for user input on wether or not the phrase is correct, and sets the input equak to 'confirm'
        if confirm.lower() == "y":
            print()
            for i in phrase:
                if i not in MORSE_CODE: #if the user input is not in the library do this
                    print(f"Sorry, I don't know how to translate {phrase}")
                else:
                    new_letter = MORSE_CODE[i] #translates to each letter to morse code
                    morse += new_letter #adds translation to string 'morse'
                    morse += ' ' #adds a space to string 'morse'
            print(morse)