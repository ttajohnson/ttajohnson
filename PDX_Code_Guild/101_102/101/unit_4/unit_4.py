# Let's play rock-paper-scissors with the computer.

#     Greet the user and use a for loop to display their possible choices.

# Welcome to Rock, Paper, Scissors!

# Your options are:

# - Rock
# - Paper
# - Scissors

# Enter your selection:  

#     The computer will ask the user for their choice (rock, paper, scissors).
#     The computer will randomly choose rock, paper or scissors.
#     Compare the players' choices and determine who won and tell the user.
import random


# print('Welcome to Rock, Paper, Scissors! \nYour options are: ')

# choices = ['Rock', 'Paper', 'Scissors']

# for choice in choices:
#     print(choice)


# user = input('Enter your selection: ')

# computer = 'Rock' #random.choice

# if user == computer:
#     print('The game is a tie!')
#     elif 

# -----------------------------------Bad Code Above for Mistake Analysis---------------------------------------#
# ----------------------------------Good Code Below for Success Analysis---------------------------------------#

print('Welcome to Rock, Paper, Scissors! \nYour choices are:')

choices = ['Rock', 'Paper', 'Scissors']

for choice in choices: #Thanks Matt!
    print(choice)

user = input('Make your selection: ')

computer = random.choice(choices) #Thanks W3 Schools!

if user == computer:
    print('The game is a draw!')
elif user == 'Rock' and computer == 'Paper':
    print(f'You chose Rock, Computer chose {computer}. You lose!')
elif user == 'Rock' and computer == 'Scissors':
    print(f'You chose Rock, Computer chose {computer}. You win!')
elif user == 'Paper' and computer == 'Scissors':
    print(f'You chose Paper, Computer chose {computer}. You lose!') #Be wary of copy and paste.
elif user == 'Paper' and computer == 'Rock':
    print(f'You chose Paper, Computer chose {computer}. You win!')
elif user == 'Scissors' and computer == 'Rock':
    print(f'You chose Scissors, Computer chose {computer}. You lose!')
elif user == 'Scissors' and computer == 'Paper':
    print(f'You chose Scissors, Computer chose {computer}. You win!')