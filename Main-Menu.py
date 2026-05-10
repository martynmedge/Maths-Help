import math
import Quadratic
import Cosine
import Sine
import grades
print("Main Menu")
print("1. Quadratic Solver")
print("2. Cosine Rule Calculator")
print("3. Sine Rule Calculator")
print("4. Grade Calculator")
print("5. Exit")
choice = input("Enter your choice (1-5): ")
if choice == "1":
    Quadratic.run()
elif choice == "2":
    Cosine.run()
elif choice == "3":
    Sine.run()
elif choice == "4":
    grades.run()
elif choice == "5":
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter a number from 1-5.")