import math
import Quadratic
import Cosine
import Sine
print("Main Menu")
print("1. Quadratic Solver")
print("2. Cosine Rule Calculator")
print("3. Sine rule Calculator")
print("4. Exit")
choice = input("Enter your choice (1-4): ")
if choice == "1":
    Quadratic.run()
elif choice == "2":
    Cosine.run()
elif choice == "3":
    Sine.run()
elif choice == "4":
    print("Exiting the program.")
else:
    print("Invalid, Please enter a number from 1-4")