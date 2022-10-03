"""
GAME: Rock Paper Scissors

"""

import random

print("Let's play rock, paper, scissors!")

choices = ["rock", "paper", "scissors"]

for choice in choices:
    print(choice)

user = input("Make your selection: ").title()

computer = random.choice(choices).title()

if user == computer:
    print("The game is a draw!")
elif user == 'Rock' and computer == 'Paper':
    print(f'You chose Rock, Computer chose {computer}. You lose!')
elif user == 'Rock' and computer == 'Scissors':
    print(f'You chose Rock, Computer chose {computer}. You win!')
elif user == 'Paper' and computer == 'Scissors':
    print(f'You chose Paper, Computer chose {computer}. You lose!')
elif user == 'Paper' and computer == 'Rock':
    print(f'You chose Paper, Computer chose {computer}. You win!')
elif user == 'Scissors' and computer == 'Rock':
    print(f'You chose Scissors, Computer chose {computer}. You lose!')
elif user == 'Scissors' and computer == 'Paper':
    print(f'You chose Scissors, Computer chose {computer}. You win!')