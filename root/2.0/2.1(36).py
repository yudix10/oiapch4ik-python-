a = float(input('Enter a - '))
b = float(input('Enter b - '))
x1 = 0
if a == 0:
    if b == 0:
        print('x любое')
    else: #bx = 0
        print('x = 0')
elif b == 0:
    print('x = 0')
else:
    x2 = -b / a
    print(f'x1 - {x1} x2 - {x2}')

