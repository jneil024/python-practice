import re

def is_strong_password(password):
    # Check for strong password criteria
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."
    return "valid"

while True:
    # Prompt user to input a password
    password = input("Enter a strong password: ")
    validation_message = is_strong_password(password)
    
    if validation_message == "valid":
        print("Password is strong!")
        break
    else:
        print(f"Invalid password: {validation_message}")
        retry = input("Do you want to try again? (Y/N): ").strip().upper()
        if retry == 'N':
            print("Goodbye!")
            break
