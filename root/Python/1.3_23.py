x1 = int(input('Enter x1 - '))
y1 = int(input('Enter y1 - '))
x2 = int(input('Enter x2 - '))
y2 = int(input('Enter y2 - '))

print((abs(x2 - x1) == 1 and abs(y2 - y1) == 2) or (abs(x2 - x1) == 2 and (abs(y2 - y1) == 1)))