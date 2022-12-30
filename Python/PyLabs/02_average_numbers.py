# LAB 02: AVERAGE NUMBERS
# Average a list of numbers.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1
# Start with a list, iterate through it, keeping a
# 'running sum', then divide that sum by the number of elements in that list.

# >>>
# nums = [5, 0, 8, 3, 4, 1, 6]

# # total = sum(nums) / len(nums)
# # print(total)

# total = 0

# for num in nums:
#     total += num

# print(total / len(nums))
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 2
# Ask the user to enter the numbers one at a time, putting them into a list.
# If the user enters 'done', then calculate and display the average.

# >>>
nums = []

while True:
    new_num = input("Enter a number or 'done': ")
    if new_num == "done":
        break
    else:
        nums.append(int(new_num))

print(sum(nums) / len(nums))
# >>>
