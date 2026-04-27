import random

def newlist():
    n = int(input('Enter number elements in list - '))
    min_range = int(input('Enter min range in list - '))
    max_range = int(input('Enter max ramge in list - '))
    list = [random.randrange(min_range, max_range) for i in range(n)]
    return list


def func(list):
    max = list[0]
    min = list[0]
    for i in list:
        if max < i:
            max = i
        elif min > i:
            min = i
    print(list)
    print(f"Min - {min}")
    print(f"Max - {max}")
    return max - min

print(func(newlist()))