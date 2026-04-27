import random
def newlist():
    n = int(input('Enter number elements in list - '))
    min_range = int(input('Enter min range in list - '))
    max_range = int(input('Enter max range in list - '))
    list = [random.randrange(min_range, max_range) for i in range(n)]
    return list

def znlist(list):
    zn = 0
    print(list)
    for i in range(1, len(list)):
        if (list[i] >= 0 and list[i - 1] >= 0) or (list[i] < 0 and list[i - 1] < 0):
            continue
        else:
            print(i - 1)
            print(f"{i}\n")
            zn += 1
    return zn

print(znlist(newlist()))