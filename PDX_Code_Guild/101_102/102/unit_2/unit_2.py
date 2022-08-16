def total(numbers):
    result = int()
    for number in numbers:
        result = result + number
    return result


numbers = [10, 10, 10, 30]

print(total(numbers))
