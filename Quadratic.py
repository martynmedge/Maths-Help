import math
print ("Quadratic Solver")
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real roots exist.")
    print(f"Root 1: {root1:.4f}")
    print(f"Root 2: {root2:.4f}")
elif discriminant == 0:
    root = -b / (2*a)
    print("One real root exists.")
    print(f"Root: {root:.4f}")
else:
    print("No real roots exist.")