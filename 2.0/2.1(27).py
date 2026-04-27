a = float(input('Enter a - '))
b = float(input('Enter b - '))
c = float(input('Enter c - '))

if a > b:
    if b > c:
        print(a + c)
    elif a > c:
        print(a + b)
    else:
        print(c + b)
elif b > c:
    if a > c:
        print(b + c)
    else:
        print(b + a)
else:
    print(c + a)