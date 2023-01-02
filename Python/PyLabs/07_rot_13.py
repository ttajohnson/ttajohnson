# LAB 07: ROT CIPHER
# Write a program that prompts the user for a string, and encodes it with ROT13.
# For each character, find the corresponding character, add it to an output
# string. Notice that there are 26 letters in the English language, so
# encryption is the same as decryption.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# >>>
import string

alphabet = string.ascii_letters
rot_alphabet = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

alpha_dict = {key: value for (key, value) in zip(alphabet, rot_alphabet)}
alpha_dict[" "] = " "

user_string = input("Message to be encoded: ")
new_string_list = []

for letter in user_string:
    new_string_list.append(alpha_dict[letter])

print("".join(new_string_list))
# >>>
