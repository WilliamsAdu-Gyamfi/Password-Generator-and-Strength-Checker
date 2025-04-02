#import random

""" picks = random.choices(range(ord('a'),ord('z')), k=8)
print(picks)
pick = [chr(i) for i in picks]
print(''.join(pick)) """


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