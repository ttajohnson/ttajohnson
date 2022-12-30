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
    card = input("What")
