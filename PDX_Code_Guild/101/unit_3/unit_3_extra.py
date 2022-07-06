import random

grade = input('How did you score on your last test from 0 - 100?')

grade = int(grade)

if grade >= 90 and grade <= 100:
    print('You have received an A')

elif grade >= 80:
    print('You have received a B')

elif grade >= 70:
    print('You have received a C')

elif grade >= 60:
    print('You have received a D')

elif grade <= 59:
    print('You have failed, your grade is an F')


rival = random.randint(0, 100)

if rival >= 90 and rival <= 100:
    print('Your rival received an A')

elif rival >= 80:
    print('Your rival received a B')

elif rival >= 70:
    print('Your rival received a C')

elif rival >= 60:
    print('Your rival received a D')

elif rival >= 59:
    print('Your rival received an F')


if grade > rival:
    print('Congratulations, you have scored higher than your rival!')

elif grade < rival:
    print('Ouch, your rival has bested you this round.')

elif grade == rival:
    print('You and your rival are equally matched!')

results = f"Your rival received a score of {rival} and you received a score of {grade}"

print(results)