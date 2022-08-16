# VERSION 1 - aces low

# def main():
#     cards = {
#         'A':1,
#         '2':2,
#         '3':3,
#         '4':4,
#         '5':5,
#         '6':6,
#         '7':7,
#         '8':8,
#         '9':9,
#         '10':10,
#         'J':10,
#         'Q':10,
#         'K':10
#     }

#     print("Need some Blackjack advice? Let's see what you've got there.")

#     c1 = cards[input('What is your first card? ').upper()]
#     c2 = cards[input('What is your second card? ').upper()]
#     c3 = cards[input('What is your third card? ').upper()]

    

#     total = c1 + c2 + c3

#     print(f"You've got a total of {total}.")

#     if total > 21:
#         print('Busted!')
#     elif total < 21 and total >= 17:
#         print('Stay')
#     elif total < 17:
#         print('Hit')
#     elif total == 21:
#         print('Blackjack!')

# main()

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# VERSION 2 - aces fluid

def card_value(card, first_sum):
    if first_sum > 10 and card == 'A':
        card = 1
    elif card == 'A':
        return 11
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    return int(card)

def main():
    
    print("Need some Blackjack advice? Let's see what you've got there.")
    c1 = input('What is your first card? ').upper()
    c2 = input('What is your second card? ').upper()
    c3 = input('What is your third card? ').upper()
    first_sum = c1 + c2 + c3
    card1 = card_value(c1, first_sum)
    card2 = card_value(c2, first_sum)
    card3 = card_value(c3, first_sum)
    total = card1 + card2 + card3
    print(f"You've got a total of {total}.")
    if total > 21:
        print('Busted!')
    elif total < 21 and total >= 17:
        print('Stay')
    elif total < 17:
        print('Hit')
    elif total == 21:
        print('Blackjack!')

main()


