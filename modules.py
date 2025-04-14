import random
import string

# All possible characters for a password
all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Auto-generate a password
password_length = random.randint(8, 15)
auto_password = "".join(random.choices(all_chars, k=password_length))
print(f"Generated Password: {auto_password}")

# Ask if the user is okay with the generated password
user_choice = input("Are you okay with this password? (yes/no): ").lower()

if user_choice == "yes":
    print(f"Great! Your password ({auto_password}) is ready to use. Stay safe online")
else:
    # Ask the user to input their own password
   # user_password = input("Enter your own password to check its strength: ")

    # Check password strength
    while True:
         user_password = input("Enter your own password to check its strength: ")
         length = len(user_password)
         has_number = any(char.isdigit() for char in user_password)
         has_upper = any(char.isupper() for char in user_password)
         has_symbol = any(char in string.punctuation for char in user_password)

   

        # Give feedback
        # print("Password Strength Check:")
         if length < 8 or not (has_number or has_upper or has_symbol):
            print(f"Your password ({user_password}) is weak. Try including numbers, symbols, and uppercase letters.")
         elif 8 <= length <= 11 and sum([has_number, has_upper, has_symbol]) >= 2:
            print(f"Your password ({user_password}) is moderate. Consider making it longer or more complex.")
            break
         elif length >= 12 and has_number and has_upper and has_symbol:
            print(f"Your password ({user_password}) is strong. Great choice!")
            break
         else:
            print(f"Your password ({user_password}) is acceptable but NOT Strong!.")
            break
