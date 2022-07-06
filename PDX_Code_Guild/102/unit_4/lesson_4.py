'''
Unit 4 - Modules
'''

"""
Modules are just Python files.
As programs grow larger, it makes sense to break them up
into separate files (modules). Modules can then be imported
into other modules using the keyword import
"""

# import the ENTIRE contents of a module into a variable
# import <MODULE_NAME>
import random
import string

# all attributes of the modules are now 
# available through the variable using a dot
letters = string.ascii_letters
random_number = random.randint(1, 100)
random_letter = random.choice(letters)

# print(random_number, random_letter, letters)

# ------------------------------------------------ #

# import SPECIFIC attributes from a module
# keywords: from / import
# from <MODULE_NAME> import <ATTRIBUTE_1>, <ATTRIBUTE_2>, ...

from string import ascii_letters # only import ascii_letters from string module
from random import randint, choice # only import randint() and choice() from random

letters = ascii_letters # shorten variable name
random_number = randint(1, 100) # don't need random.randint() anymore
random_letter = choice(letters)

# print(random_number, random_letter, letters)

# ------------------------------------------------- #

# import SPECIFIC attributes from a module 
# and change their variable name
# keywords: from / import / as
# from <MODULE_NAME> import <ATTRIBUTE_NAME> as <VARIABLE_NAME>

from string import ascii_letters as letters
from random import randint as r_int, choice as r_ch

random_number = r_int(1, 100)
random_letter = r_ch(letters)
# print(random_number, random_letter, letters)