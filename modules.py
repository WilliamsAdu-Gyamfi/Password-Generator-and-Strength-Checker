import random
import string

all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
print(all_chars)
print(len(all_chars))

# password length (minimum of 8 and maximum of 15)
pwl = random.randint(8,15)
print(pwl)

# random select characters
pwc = random.choices(all_chars, k = pwl)

# join the characters into a single password string
pw = "".join(pwc) 

# print the generated password
print(pw)

# User inputs

# Ask the user how many passwords they want to generate
gen_pw = int(input("Enter the number of password you want to generate: "))

# Ask the user for a preferred length (between 8 and 15).
pw_len = int(input("Enter a preferred pssword length (between 8 and 15): "))

# Generate that many passwords
if pw_len >= 8 and pw_len <= 15:
    
   """ for _ in range(gen_pw):
        password = "".join(random.choices(all_chars, k=pw_len))
        # Print them all
        print(password) """
   
   # Alterative Method(Printing te number of password generated - Using an Index Variable)
   for i in range(gen_pw):
        password = "".join(random.choices(all_chars, k=pw_len))
        print(f"Password {i+1}: {password}")
    
else:
   # Handle invalid input
   print("Error: Password length must be between 8 and 15")


# CHECKING PASSWORD STRENGTH

# Ask the user to enter a password to check its strength.
pws = input("Enter a password to check its strength: ")

# Check its length (less than 8, 8-11, or 12+ characters).
length = len(pws)
has_number = any(char.isdigit() for char in pws)
has_upper = any(char.isupper() for char in pws)
has_symbol = any(char in string.punctuation for char in pws)

# Check password strength
if length < 8 or not(has_number or has_upper or has_symbol):
    print(f"Your password {pws} is weak (It must be at least 8 characters and include numbers, uppercase, or symbols)")
elif length >= 8 and length <= 11 and sum([has_number, has_upper, has_symbol]) > 2:
    print(f"Your password {pws} is moderate. (Try adding a symbol or number to make it stronger)")
elif length >= 12 and has_number and has_upper and has_symbol:
     print(f"Your password '{pws}' is Strong (Great job! This is a secure password).")
else:
    print(f"Your password {pws} is strong")

