import random
def newlist():
    n = int(input('Enter number elements in list - '))
    min_range = int(input('Enter min range in list - '))
    max_range = int(input('Enter max range in list - '))
    list = [random.randrange(min_range, max_range) for i in range(n)]
    return list

def prost_num(list):
    sum = 0
    counter = 0


print(prost_num(newlist()))
