#import random

""" picks = random.choices(range(ord('a'),ord('z')), k=8)
print(picks)
pick = [chr(i) for i in picks]
print(''.join(pick)) """
for i in range(5):  # We only care about repeating 5 times, not the index
    print("Hello!")


import random
import string

all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# password length
pwl = random.randint(8,15)

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
   
   # Alterative Method(Printing te number of password generated)
   for i in range(gen_pw):
        password = "".join(random.choices(all_chars, k=pw_len))
        print(f"Password {i+1}: {password}")
    


else:
   # Handle invalid input
   print("Error: Password length must be between 8 and 15")

