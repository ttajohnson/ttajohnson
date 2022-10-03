"""
CC Validation

"""
# Valid 4556737586899855
# Inv   4556737586899859

def sub_nine(card_number):
    for i in range(len(card_number)): #Iteration through list of numbers.
        if card_number[i] > 9: # If a number in the list is greater than 9,
            card_number[i] -= 9 # Subtract 9 from that number.
    return card_number # Return the list after subtractions.

def credit_card_validator():
    card_number = [] # Create an empty list.
    card_number = input("Enter your credit card number: ") # Take in a cc number.
    card_number = [int(num) for num in card_number] # Convert each individual number into an integer element of the list.
    check_digit = card_number.pop() # Pop out the last digit for later use.
    card_number = card_number[::-1] # Reverse the list.
    card_number = [num*2 if index %2 == 0 else num for index, num in enumerate(card_number)]
    card_number = sub_nine(card_number) # Sub_nine method.
    summed = sum(card_number) # Summed list.
    second_digit = summed%10 # Grabbing second digit from sum.
    if second_digit == check_digit: # Using check-digit.
        return True and print('Valid Credit Card Number')
    else: print("Invalid Credit Card Number")

credit_card_validator()