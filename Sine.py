print ("Sine Rule Calculator")
print ("1 - Input to Calculate the length of a side")
print ("2 - Input to Calculate an angle")
choice = input("Enter 1 or 2: ")
if choice == "1":
    a = float(input("Enter the length of side a: "))
    A = float(input("Enter the measure of angle A in degrees: "))
    B = float(input("Enter the measure of angle B in degrees: "))
    import math
    A_rad = math.radians(A)
    B_rad = math.radians(B)
    b = (a * math.sin(B_rad)) / math.sin(A_rad)
    print(f"The length of side b is: {b:.2f}")

elif choice == "2":
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    A = float(input("Enter the measure of angle A in degrees: "))
    import math
    A_rad = math.radians(A)
    B_rad = math.asin((b * math.sin(A_rad)) / a)
    B = math.degrees(B_rad)
    print(f"The measure of angle B is: {B:.2f} degrees")