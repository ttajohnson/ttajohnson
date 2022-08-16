def total(numbers):
    result = int()
    for number in numbers:
        result = result + number
    return result


numbers = []

while True:
    choice = input('Enter a number or "done" to quit: ')
    if choice == "done":
        break
    choice = int(choice)
    numbers.append(choice)
print(f'You entered {numbers}')
print(f'The sum of the numbers is {total(numbers)}')