import math

x1 = float(input("Enter x1 - "))
y1 = float(input("Enter y1 - "))
x2 = float(input("Enter x2 - "))
y2 = float(input("Enter y2 - "))

A = math.sqrt(x1**2 + y1**2)
B = math.sqrt(x2**2 + y2**2)

if A == B:
    print('A и B равноудалены')
elif A < B:
    print('A ближе')
else:
    print('B ближе')