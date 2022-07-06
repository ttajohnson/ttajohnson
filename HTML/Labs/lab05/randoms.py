import string
import random

class Randoms:
    def __init__(self):
        return
    
    def random_characters(self, length, alphabet):
        output = ''
        for i in range(length):
            char = random.choice(alphabet)
            output += char
        return output

    def random_password(self, uppers, lowers, nums, special):
        output = ''
        output += self.random_characters(uppers, string.ascii_uppercase)
        output += self.random_characters(lowers, string.ascii_lowercase)
        output += self.random_characters(nums, string.digits)
        output += self.random_characters(special, string.punctuation)
        output = list(output)
        random.shuffle(output)
        output = ''.join(output)
        print(output)
        return output

def method():
    print("Randoms")