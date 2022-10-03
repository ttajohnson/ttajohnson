"""
Average Numbers

"""

def average():
    nums = []
    while True:
        num = input("Enter a number, or 'done': ")
        if num == "done":
            break
        nums.append(int(num))

    total = 0

    for num in nums:
        total += num
    
    print(f"The sum of your numbers is {total}.")
    elements = len(nums)
    print(f"You have {elements} numbers in your list.")
    average = total / elements
    print(f"The average of your numbers is {average}")

average()