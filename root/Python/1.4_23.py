x = int(input("Enter x - "))
y = int(input("Enter y - "))

print((x <= (x**2 + y**2 == 36) and y <= (x**2 + y**2 == 36) and x >= (x**2 + y**2 == 9) and y >= (x**2 + y**2 == 36) and x >= 0 and y >= 0) or
(x >= 0 and abs(x <= (x**2 + y**2 == 36)) and abs(y <= (x**2 + y**2 == 36))))