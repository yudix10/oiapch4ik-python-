x = float(input('Enter x - '))
y = float(input('Enter y - '))
d1 = (y >= 0 and (abs(x) <= 1))
d2 = x**2 + (y - 1)**2 >= 1
print(d1)
print(d2)
print(d1 and d2)
