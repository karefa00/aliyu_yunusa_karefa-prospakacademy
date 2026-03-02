# Grade Evaluator with Conditionals

# Get Input
try:
    score = int(input("Enter the student's numerical score (0-100): "))
except ValueError:
    print("Invalid input. Please enter an integer between 0 and 100.")
    exit()  # Exit program if input is not an integer

# Input Validation
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    exit()

# Grade Evaluation
if score >= 90:
    print("The grade is: A")
    # Nested Conditional for 'A' Grade
    if score == 100:
        print("Perfect Score! Excellent work!")
    elif 90 <= score <= 94:
        print("Great start to an A! Keep it up!")
    else:  # 95-99
        print("Solid A! Well done!")

elif score >= 80:  # B grade
    print("The grade is: B")
elif score >= 70:  # C grade
    print("The grade is: C")
elif score >= 60:  # D grade
    print("The grade is: D")
else:  # F grade
    print("The grade is: F")