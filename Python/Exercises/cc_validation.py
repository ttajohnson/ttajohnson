""" Python Exercise - Credit Card Validation
    
    Instructions: Write a function that returns whether a string containing a credit card number is valid as a boolean.

        1. Convert the input string into a list of ints.
        2. Slice off the last digit. That is the 'check digit'.
        3. Reverse the digits.
        4. Double every other element in the reversed list, starting with index 0.
        5. Subtract 9 from numbers > 9.
        6. Sum
        7. Isolate the second digit of that sum.
        8. Check if the isolated digit matches the 'check digit'. If so, the Credit Card Number is valid.

    Example Valid CC: 4556737586899855
    Example Invalid CC: 4556737586899854
"""

def main():
    

    # Ask the user for a CC number. Dislcaimer for fun + save dingus'.
    print("DISCLAIMER: This is a Python Exercise ONLY.\nIf you encounter and run this file, DO NOT enter your real credit card number.\nBe mindful.")
    cc_input = input("Please Enter Your Credit Card Number: ")

    # Convert the string into a list of integers.
    cc_number = [int(char) for char in cc_input]
    # print(cc_number)

    # Slice off the 'check digit'.
    check_digit = cc_number.pop()
    # print(check_digit)

    # Reverse the list.
    reverse_cc = cc_number[::-1]
    # print(reverse_cc)
    
    # Double every other number. At this point I'm choosing to use enumerate() and comprehension.
    doubled_list = [num * 2 if index % 2 == 0 else num for index, num in enumerate(reverse_cc)]
    # print(doubled_list)

    # Subtract 9 from any number > 9.
    sub_9 = [num - 9 if num > 9 else num for num, num in enumerate(doubled_list)]
    # print(sub_9)

    # Sum the entire list.
    sum_num = sum(sub_9)
    # print(sum_list)

    # Isolate the second digit of the sum.
    sec_digit = sum_num % 10

    # Check if the isolated digit matches the check digit.
    if check_digit == sec_digit:
        print("Valid Credit Card Number Accepted!")
    else:
        print("Invalid Credit Card Number!")


if __name__ == "__main__":
    main()





