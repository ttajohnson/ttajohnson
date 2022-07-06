# VERSION 1 - given list of nums

# def v1_average_numbers():
#     nums = [5, 0, 8, 3, 4, 1, 6]
#     print(f'Your numbers are {nums}')
#     total = sum(nums)
#     print(f'The total sum is {total}')
#     i = len(nums)
#     result = total/i
#     print(f'The average of these numbers is {result}')

# v1_average_numbers()

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# VERSION 2 - enter list

def main():
    nums = []
    print("Let's average some numbers!")

    while True:
        try:
            number = input('Enter a number, or "done": ').lower()
            if number == 'done':
                break
            else:
                nums.append(int(number))
        except ValueError as e:
            print(e)
            print('Please enter a number or "done" to stop...')
            pass
        
    total = sum(nums)
    i = len(nums)
    result = total / i

    print(f'Your numbers are {str(nums)} \nThe sum of your numbers is {total} \nThe average of your numbers is {result}')

main()

        


