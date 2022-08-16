# ....Lab 05 Version 1

import random

# generate a list of 6 random numbers (COMPLETE)
def pick6():
    x = []
    for _ in range(6):
        r = random.randint(1, 99)
        x.append(r)
    return x

# money = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

# define a function to match winning ticket to user ticket (COMPLETE)
def num_matches(winning, ticket):
    money = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1
        earnings = money[matches]
    return earnings

# Run a Pick6 lottery game 100,000 for sad results, try not to get obsessed with running... (COMPLETE)
# def lottery():
#     wallet = 0
#     winner = 0
#     winning = pick6()
#     for i in range(100000):
#         ticket = pick6()
#         wallet = wallet - 2
#         winner += num_matches(winning, ticket)   
#     final_balance = wallet + winner
#     return final_balance




# print(lottery())

# ....Lab 05 Version 2 - ROI (COMPLETE)

def lottery():
    wallet = 0
    winner = 0
    expenses = 0
    winning = pick6()
    for _ in range(100000):
        ticket = pick6()
        wallet = wallet - 2
        expenses = expenses + 2
        winner += num_matches(winning, ticket)   
    final_balance = wallet + winner
    roi = (winner - expenses)/expenses
    return print(f'Your final balance is ${final_balance}, your earnings were ${winner}, your expenses were ${expenses}. Your ROI is {roi}%.')

lottery()