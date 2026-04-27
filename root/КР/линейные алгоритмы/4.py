import math

x = float(input('Enter x - '))
y = float(input('Enter y - '))

p = math.sqrt(x**2 + y**2)
f = math.atan(y/x)
print(p,f)