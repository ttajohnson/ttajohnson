"""
Random Password Generator

"""

import random
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
all_characters = letters + digits + punctuation

password = []
n = int(input("How many characters does your password need: "))


while len(password) < n:
    password.append(random.choice(all_characters))

print(''.join(password))