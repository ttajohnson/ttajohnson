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

user_choice = input("How many characters do you want your password to be?: ")

password = []

while len(password) < int(user_choice):
    password.append(random.choice(all_characters))
    if len(password) >= int(user_choice):
        break
print(''.join(password))

# GREAT SUCCESS! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~