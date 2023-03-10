#type:ignore
import board
import time
import digitalio

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

# The Morse code timing rules we will use for signaling are: 
# a dot (.) lasts for 1/4 second. a dash (-) lasts for 3/4 seconds. 
# the space between dots and dashes that are part of the same letter is 1/4 second.
# space between letters is 3/4 seconds
# space between words is 1+3/4 seconds

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT 

led.value = False

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
            for i in morse:
                if i == "-":
                    led.value = True
                    time.sleep(dash_time)
                    led.value = False
                if i ==".":
                    led.value= True
                    time.sleep(dot_time)
                    led.value = False
                if i == " ":
                    led.value = True
                    time.sleep(between_letters)
                if i == "/":
                    led.value = False
                    time.sleep(between_words)
                time.sleep(between_taps)