def func(num):
    dividers = 0
    while dividers != 2:
        num += 1
        for i in range(1, num + 1):
            if num % i == 0:
                dividers += 1
        if dividers > 2:
            dividers = 0
    return num

print(func(2))
