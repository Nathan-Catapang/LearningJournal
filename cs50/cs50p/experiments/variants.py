# Version 1: Using if-elif-else statements
# This is a straightforward approach to determine the grade based on the score input by the user.

score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:

    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



# Version 2: Using a dictionary to map score ranges to grades
# Note: This approach is less efficient than the if-elif-else structure for this specific case, but it demonstrates how to use a dictionary for mapping.

score = int(input("Enter your score: "))

grades = {
    range(90, 101): "A",
    range(80, 90): "B",
    range(70, 80): "C",
    range(60, 70): "D",
    range(0, 60): "F"
}

for r, grade in grades.items():
    if score in r:
        print("Grade:", grade)
        break



# Using a loop to check score against cutoffs
# This approach is more scalable and easier to maintain if you have many grade cutoffs.

score = int(input("Enter your score: "))

grading = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F")
]

for cutoff, grade in grading:
    if score >= cutoff:
        print("Grade:", grade)
        break
