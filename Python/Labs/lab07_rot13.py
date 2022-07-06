# ....Lab 07 Version 1

# Version 1 using dictionary.
# def rot13_dictionary():
#     alph_rot = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 
#     'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', ' ': ' ' }
#     user_input = input("Type your messsage to be encrypted: ")
#     list(user_input)
#     for letter in user_input:
#         print(alph_rot[letter], end= '')

# Version 2 using two strings.
def rot13_strings():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    alphabet_rot = "nopqrstuvwxyzabcdefghijklm "
    user_input = input("Type message to encrypt: ")
    output = ''
    for letter in user_input:
        index = alphabet.find(letter)
        output += alphabet_rot[index]
    print(output)


# rot13_dictionary()

rot13_strings()