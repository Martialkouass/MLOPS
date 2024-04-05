# we are developing an application, where users need to register.
# They need to fill in their username, email and password.

import re
import getpass

def validate_username(username):
    if not username:
        return False
    if ' ' in username:
        return False
    if not username.isalnum():  # Check if username contains only alphanumeric characters
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char in r'!@#$%^&*()-_=+[\]{}|;:,.<>?`~' for char in password):
        return False
    return True

def validate_email(email):
    if '@' not in email or '.' not in email:
        return False
    return True


def register():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")  # Using getpass to hide password input
    return username, email, password

def main():
    username, email, password = register()
    print("Username:", username)
    print("Email:", email)
    print("Password:", password)
    if not validate_username(username):
        print("Invalid username. Username should not be empty and should not contain spaces.")
    elif not validate_email(email):
        print("Invalid email. Email should contain '@' and '.'.")
    elif not validate_password(password):
        print("Invalid password. Password should be at least 8 characters long and contain at least one number, one letter, and one special character.")
    else:
        print("Registration successful!")

if __name__ == "__main__":
    main()
    
    
    
    
    