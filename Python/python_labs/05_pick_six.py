# LAB 05: PICK SIX
# Initially the program will pick 6 random numbers as the 'winner'.
# Then try playing pick6 100,000 times, with the ticket cost and payoff below:
## a ticket costs $2
## if 1 number matches, you win $4
## if 2 numbers match, you win $7
## if 3 numbers match, you win $100
## if 4 numbers match, you win $50,000
## if 5 numbers match, you win $1,000,000
## if 6 numbers match, you win $25,000,000

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# >>>
import random

## def random_nums():
##     num_list = []
##     while len(num_list) < 5:
##         num = random.randint(1, 99)
##         num_list.append(num)
##     return num_list


def random_nums():
    num_list = [random.randint(1, 99) for num in range(5)]
    return num_list


def ticket_compare(winning, play):
    prizes = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}
    matches = 0
    for i in range(len(play)):
        if winning[i] == play[i]:
            # print(winning, play)
            matches += 1
            # print(f"Matches: {matches}")
        earnings = prizes[matches]
        # print(f"Earnings: ${earnings}")
    return earnings


def main():
    counter = 0
    balance = 0
    winning_ticket = random_nums()

    while counter < 100000:
        play_ticket = random_nums()
        balance -= 2
        # print(balance)
        earnings = ticket_compare(winning_ticket, play_ticket)
        balance += earnings
        counter += 1
    print(f"\nWinning Numbers: {winning_ticket}\nPlays: {counter}\nPayout: ${balance}")


main()
# >>>
