import math

print("Grade Calculator")
print("1. Calculate Grade from Percentage")
print("2. Calculate Grade from Marks")
choice = input("Enter your choice (1-2): ") 

if choice == "1":
    percentageA = float(input("Enter the percentage for A: "))
    percentageB = float(input("Enter the percentage for B: "))
    percentageC = float(input("Enter the percentage for C: "))
    percentageD = float(input("Enter the percentage for D: "))
    percentage = float(input("Enter the percentage: "))
    if percentage >= percentageA:
        grade = "A"
    elif percentage >= percentageB:
        grade = "B"
    elif percentage >= percentageC:
        grade = "C"
    elif percentage >= percentageD:
        grade = "D"
    else:
        grade = "F"
    print(f"The grade is: {grade}")

elif choice == "2":
    marksA = float(input("Enter the marks needed for an A: "))
    marksB = float(input("Enter the marks needed for a B: "))
    marksC = float(input("Enter the marks needed for a C: "))
    marksD = float(input("Enter the marks needed for a D: "))
    totalMarks = float(input("Enter the total marks: "))
    obtainedMarks = float(input("Enter the obtained marks: "))
    percentage = (obtainedMarks / totalMarks) * 100
    if percentage >= (marksA / totalMarks) * 100:
        grade = "A"
    elif percentage >= (marksB / totalMarks) * 100:
        grade = "B"
    elif percentage >= (marksC / totalMarks) * 100:
        grade = "C"
    elif percentage >= (marksD / totalMarks) * 100:
        grade = "D"
    else:
        grade = "F"
    print(f"The grade is: {grade}")
else:
    print("Invalid choice. Please enter 1 or 2.")