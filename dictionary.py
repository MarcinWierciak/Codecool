
import sys
import csv

while True:
    with open('dii.csv', mode='r+') as dict_file: # Opening a file in read and write mode, naming an opened file "dict_file"
        reader = csv.reader(dict_file)
        writer = csv.writer(dict_file)
        my_dict = {rows[0]:rows[1:] for rows in reader} # Creating a dictionary from opened file. Keys = first argument in a line, expln and source = second and third arguments in a line
        print("\nDictionary for a little programmer:\n1) search explanation by appellation\n2) add new definition\n3) show all appellations alphabetically\n0) exit\n")
        menu_key = input() # Input for menu key

        if menu_key == "1":
            try:
                word = input() # Input for a word from dictionary
                print(my_dict[word]) # Print for a definition for entered word
            except KeyError: # Secure for key errors :)
                print("\nWrong word! Try again.")

        elif menu_key == "2":
            new_word = input("Enter a new word: ") # New word for a dictionary
            new_definition = input("Enter a new definition: ") # New definition for a dictionary
            new_source = input("Enter a new source: ") # New source for a dictionary
            writer.writerow([new_word,new_definition,new_source]) # Writing a new line with enetered data, adding these things to dictionary
            print("Your new definition is in dictionary!")

        elif menu_key == "3":
            print(list(sorted(my_dict.keys()))) # Sorting list of keys alphabetically

        elif menu_key == "0":
            print("\nBye.")
            sys.exit()

        else:
            print("\nWrong key! Try again.")
