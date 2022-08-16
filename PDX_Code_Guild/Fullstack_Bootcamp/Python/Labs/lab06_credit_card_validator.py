# ....Lab 06 Version 1 (COMPLETE)

def sub_nine(card_number):
    for i in range(len(card_number)): #looking at the whole list of numbers
        if card_number[i] > 9: #if a number in the list is greater than 9
            card_number[i] -= 9 #subtract 9 from that number
    return card_number #return the list after subtractions

def credit_card_validator():
    card_number = [] #create an empty list
    card_number = input("Enter your credit card number: ") #take in a cc number
    card_number = [int(num) for num in card_number] #convert each individual number into an integer element of the list
    check_digit = card_number.pop() #pop out the last digit for later use
    card_number = card_number[::-1] #reverse the list
    card_number = [num*2 if index %2 == 0 else num for index, num in enumerate(card_number)]
        # for i, n in enumerate(card_number):
    #     print(i, n)\
    card_number = sub_nine(card_number) #see sub_nine function
    summed = sum(card_number)
    second_digit = summed%10
    if second_digit == check_digit:
        return True and print('Valid Credit Card Number')
    else: print("Invalid Credit Card Number")



    
    # print(second_digit)   
    # print(card_number)
    # print(summed)
    # print(check_digit)


credit_card_validator()


