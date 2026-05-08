print("Cosine Rule Calculator")
print("1 - Input to Calculate the length of a side")
print("2 - Input to Calculate an angle")

choice = input("Enter 1 or 2: ")
print(choice)
if choice == "1":
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    C = float(input("Enter the measure of angle C in degrees: "))
    import math
    C_rad = math.radians(C)
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))
    print(f"The length of side c is: {c:.2f}")

elif choice == "2":
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    import math
    A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    print(f"The measure of angle A is: {A:.2f} degrees")