import random

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