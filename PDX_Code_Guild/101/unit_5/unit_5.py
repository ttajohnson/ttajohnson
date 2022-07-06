# Let's generate a ten-character password using a while loop and random.choice().

# The final result will be a string of random characters all on one line.

# Example output:

# Your password: Q45pA%x9PJ

# Extra Challenge 1

# Allow the user to choose how many characters the password will be.
# Extra Challenge 2

# Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().





import random
import string

letters = string.ascii_letters
# print(letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

digits = string.digits
# print(digits) # '0123456789'

punctuation = string.punctuation
# print(punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

all_characters = letters + digits + punctuation
# print(all_characters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

password = []

while len(password) < 10:
    password.append(random.choice(all_characters))

print(''.join(password))

# GREAT SUCCESS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~