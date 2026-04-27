import random
n = int(input('Enter number elements in list - '))
list = [float(random.randrange(-10, 10)) for i in range(n)]

def func(list):
    plus = 0
    minus = 0
    zero = 0
    for i in list:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            zero += 1
    print(list)
    print(f"Plus - {plus}\nMinus - {minus}\nZero - {zero}")

func(list)