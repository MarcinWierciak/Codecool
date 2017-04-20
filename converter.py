# SMNSC
import sys

def bin_to_dec(number): # Function that converting binary number to decimal number
        decimal = 0
        binary_s = str(number)
        if number ==0: # To print "0" when input is "0"
            print("\n/-------" + "".join("-" * len(str(decimal))) + "\\\n| 0 | 10 |\n\\-------" + "".join("-" * len(str(decimal))) + "/")
        else:
            for digit in binary_s:
                decimal = decimal*2 + int(digit) # Converts binary to decimal in a simply way without using build in functions
            print("\n/-------" + "".join("-" * len(str(decimal))) + "\\\n| " + str(decimal) + " | 10 |\n\\-------" + "".join("-" * len(str(decimal))) + "/")

def dec_to_bin(number): # Function that converting decimal number to binary number
    binary_l=[]
    if number == 0: # To print "0" when input is "0"
        print("\n/-------" + "".join("-" for digit in binary_l) + "\\\n| 0 | 2 |\n\\-------" + "".join("-" for digit in binary_l) + "/")
    else:
        while number > 0: # Converts decimal to binary in a simply way without using build in functions
            value = int(number % 2)
            number = int(number / 2)
            binary_l.append(value)
        binary_l.reverse()
        print("\n/------" + "".join("-" for digit in binary_l) + "\\\n|", "".join(str(digit) for digit in binary_l) + " | 2 |\n\\------" + "".join("-" for digit in binary_l) + "/")

def error_quit(): # Function that shows every time input is wrong
    again = input("\nWrong!\nEnter a number,\nPress 'SPACEBAR',\nEnter an actual numeral system ('10' for decimal or '2' for binary).\n\n'Q/q' for QUIT or any other key for try again.").upper()
    if again=="Q":
        sys.exit()
    else:
        pass

print("\nWelcome to SMNSC - super minimalistic numeral system converter!\nFirst: Enter a number,\nSecond: Press SPACEBAR,\nThird: Enter an actual numeral system ('10' for decimal or '2' for binary).")
while True:
    try:
        line = input("\n").split(" ") # Splitting input by space into two arguments
        number = int(line[0]) # Number we want to convert is a first argument
        if len(line) ==2: # If line has only two arguments separated by space
            numeral_system = line[1] # Actual numberal system,
            binary_system = "01"
            if int(numeral_system) == 2 and set(str(number))==set(binary_system): # Checking if numeral system for binary is correct
                bin_to_dec(number)
            elif int(numeral_system) == 10: # Checking if numeral system for decimal is correct
                dec_to_bin(number)
            else: # Incorrect numeral system for number or incorrect input
                error_quit()
        else: # If line has other then two arguments separated by space
            error_quit()
    except ValueError: # Secure for value errors :)
        error_quit()
