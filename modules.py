import random
import string

# All characters for password generation
all_chars = string.ascii_letters + string.digits + string.punctuation

# Function to generate password(s)
def generate_passwords():
    #try:
        gen_pw = int(input("Enter the number of passwords you want to generate: "))
        pw_len = int(input("Enter the preferred password length (between 8 and 15): "))

        if 8 <= pw_len <= 15:
            for i in range(gen_pw):
                password = "".join(random.choices(all_chars, k=pw_len))
                print(f"Password {i+1}: {password}")
        else:
            print(" Error: Password length must be between 8 and 15.")
    #except ValueError:S
     #   print(" Invalid input! Please enter a number.")

# Function to check password strength
def check_password_strength():
    password = input("Enter a password to check its strength: ")
    length = len(password)
    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Check password strength
    if length < 8 or not (has_number or has_upper or has_symbol):
        print(f"Your password '{password}' is Weak (less than 8 characters or missing complexity).")
    elif 8 <= length <= 11 and sum([has_number, has_upper, has_symbol]) >= 2:
        print(f"Your password '{password}' is Moderate.")
    elif length >= 12 and has_number and has_upper and has_symbol:
        print(f"Your password '{password}' is Strong! Great job.")
    else:
        print(f"Your password '{password}' is OK but could be improved.")

# Main loop
while True:
    print("What would you like to do?")
    print("1. Generate a Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        generate_passwords()
    elif choice == "2":
        check_password_strength()
    elif choice == "3":
        print("Okay! You are safe")
        break
    else:
        print("Invalid choice. Please enter the required number(1, 2, or 3) ")
