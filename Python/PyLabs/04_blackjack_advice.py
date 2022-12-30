# LAB 04: BLACKJACK ADVICE
# Let's write a python program to give basic blackjack playing advice during a
# game by asking the player for cards. First, ask the user for three playing
# cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point
# value of each card individually. Number cards are worth their number, all
# face cards are worth 10. At this point, assume aces are worth 1.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1

# >>>
face_cards = {"A": 1, "J": 10, "Q": 10, "K": 10}
hand = []

while True:
    card = input("Card: ").capitalize()
    if card in face_cards.keys():
        card = face_cards[card]
    else:
        card = int(card)
    hand.append(card)
    if len(hand) == 3:
        break

total = sum(hand)

print(*hand, sep=" + ")

print(total)

if total < 17:
    print("Hit")
elif total >= 17 and total < 21:
    print("Stay")
elif total == 21:
    print("Blackjack!")
else:
    print("Busted")
# >>>
