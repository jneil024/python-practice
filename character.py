import re

while True:
    # Ask for user input
    user_input = input("Enter a character: ")
    
    # Check and classify the character
    if re.match(r'^[a-zA-Z]$', user_input):
        print("The character is an alphabet.")
    elif re.match(r'^[0-9]$', user_input):
        print("The character is numeric.")
    elif re.match(r'^[a-zA-Z0-9]$', user_input):
        print("The character is alphanumeric.")
    else:
        print("The character is a special character.")
    
    # Ask if the user wants to try again
    while True:
        retry = input("Do you want to try again? (Y/N): ").strip().upper()
        if retry == 'Y':
            break  # Go back to the start of the loop
        elif retry == 'N':
            print("Goodbye!")
            exit()  # Exit the program
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
