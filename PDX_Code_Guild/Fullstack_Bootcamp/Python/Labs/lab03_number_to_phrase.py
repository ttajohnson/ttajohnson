# VERSION 1 - 0-99

# def main():

#     numphrase1 = {
#         1:'one',
#         2:'two',
#         3:'three',
#         4:'four',
#         5:'five',
#         6:'six',
#         7:'seven',
#         8:'eight',
#         9:'nine',
#         0:'',
#         10:'ten',
#         11:'evelen',
#         12:'twelve',
#         13:'thirteen',
#         14: 'fourteen',
#         15:'fifteen',
#         16:'sixteen',
#         17:'seventeen',
#         18:'eighteen',
#         19:'nineteen',
#         20:'twenty',
#         30:'thirty',
#         40:'forty',
#         50:'fifty',
#         60:'sixty',
#         70:'seventy',
#         80:'eighty',
#         90:'ninety'
#     }

#     num = int(input('Enter a number: '))

#     ones_digit = num%10
#     tens_digit = num//10

#     if num >= 0 and num <=19:
#         print(numphrase1[num])
#     elif num > 19 and num < 100:
#         print(numphrase1[tens_digit * 10] + ' ' + numphrase1[ones_digit])

# main()

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# VERSION 2 - 0-999

def main():

    ones = {0:' ', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    tens = {0:' ', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

    num = int(input("Give me a number: "))
    hundreds_digit = num//100
    tens_digit = num%100//10
    huntens_digit = num%100
    ones_digit = num%10

    if num == 0:
        print('zero')
    elif num in range(10):
        print(ones[num])
    elif num in range(10, 20):
        print(teens[num])
    elif num in range(20, 100):
        print(tens[tens_digit] + ' ' + ones[ones_digit])
    elif num in range(100, 1000):
            if tens_digit == 1:
                print(ones[hundreds_digit] + ' hundred ' + teens[huntens_digit])
            else: print(ones[hundreds_digit] + ' ' + 'hundred' + ' ' + tens[tens_digit] + ' ' + ones[ones_digit])

main()