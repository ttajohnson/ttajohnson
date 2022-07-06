# # Grading

# Let's convert a numerical score into a letter grade, using if and elif statements and comparisons.

#     Have the user enter a number representing the score (0-100)
#     Convert the score to a letter grade A - F

# Numeric Ranges

#     90-100: A
#     80-89: B
#     70-79: C
#     60-69: D
#     0-59: F

# Extra Challenge 1

# Use the random module's randint() function to determine the user's rival's score.

#     Grade the rival's score as well
#     Compare the user's score to the rival's score
#     Let the user know if they did better than their rival.
#     Display the result along with both student's scores and letter grades.

# Extra Challenge 2

# Use % to get the remainder of the grade when divided by ten, which is the same as the number in the ones digit. The number in the ones digit will determine whether they will get a '+' or a '-' appended to the end of their grade.

# For example, the grade 81 would be a 'B'. 81 % 10 would give you 1, which is a low number, so you would add a '-' to the end of the grade.

grade = input('How did you score on your last test from 0 - 100?')

grade = int(grade)

if grade >= 90 and grade <= 100:
    print('You have received an A')

elif grade >= 80:
    print('You have received a B')

elif grade >= 70:
    print('You have received a C')

elif grade >= 60:
    print('You have received a D')

elif grade <= 59:
    print('You have failed, your grade is an F')