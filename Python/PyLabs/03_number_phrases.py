# LAB 03: NUMBER PHRASES
# Convert a given number into its english representation.
# For example: 67 becomes 'sixty-seven'.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1
# Handle numbers from 0-99.

# >>>
ones_list = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

rowdy_teens = [
    "",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tens_list = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


x = input("Number: ")
x = int(x)
tens_digit = (x // 10) % 10
ones_digit = x % 10

# if x == 0:
#     print("zero")
# elif x > 10 and x < 20:
#     print(rowdy_teens[ones_digit])
# else:
#     print(tens_list[tens_digit], ones_list[ones_digit])
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 2
# Handle numbers from 100-999.

# >>>
hundreds_digit = (x // 100) % 10

if x == 0:
    print("zero")
elif x > 10 and x < 20:
    print(rowdy_teens[ones_digit])
elif hundreds_digit > 0:
    if tens_digit == 1 and ones_digit > 0:
        print(f"{ones_list[hundreds_digit]} hundred {rowdy_teens[ones_digit]}")
    else:
        print(
            f"{ones_list[hundreds_digit]} hundred {tens_list[tens_digit]} {ones_list[ones_digit]}"
        )
else:
    print(tens_list[tens_digit], ones_list[ones_digit])
