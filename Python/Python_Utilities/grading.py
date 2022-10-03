"""
Grading
"""

def grade():
    number_score = int(input("What is your number score: "))

    if number_score >= 90:
        letter_grade = "A"
    elif number_score >= 80 and number_score <= 89:
        letter_grade = "B"
    elif number_score >= 70 and number_score <= 79:
        letter_grade = "C"
    elif number_score >= 60 and number_score <= 69:
        letter_grade = "D"
    elif number_score <= 59:
        letter_grade = "F"

    print(f"You got a(n) {letter_grade}")

grade()

