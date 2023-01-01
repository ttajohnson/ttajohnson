# LAB 06: CREDIT CARD VALIDATION
# Let's write a function credit_card_validator which returns whether a string
# containing a credit card number is valid as a boolean.

# The steps are as follows:
# 1. Convert the input string into a list of ints
# 2. Slice off the last digit. That is the check digit.
# 3. Reverse the digits.
# 4. Double every other element in the reversed list (starting with the first number in the list).
# 5. Subtract nine from numbers over nine.
# 6. Sum all values.
# 7. Take the second digit of that sum.
# 8. If that matches the check digit, the whole card number is valid.
# Here is a valid credit card number to test with: 4556737586899855

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# >>>
credit_card = 4556737586899855


def cc_validator(cc):
    cc_list = [int(num) for num in str(credit_card)]
    check_digit = cc_list.pop()
    cc_list.reverse()
    cc_list = [num * 2 if index % 2 == 0 else num for index, num in enumerate(cc_list)]
    for i in range(len(cc_list)):
        if cc_list[i] > 9:
            cc_list[i] = cc_list[i] - 9
    cc_list = sum(cc_list)
    ones_digit = cc_list % 10
    if ones_digit == check_digit:
        print("Credit Card Valid!")
    else:
        print("Invalid!")


cc_validator(credit_card)
# >>>
