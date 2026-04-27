import random

def newlist():
    n = int(input('Enter number elements in list - '))
    min_range = int(input('Enter min range in list - '))
    max_range = int(input('Enter max ramge in list - '))
    list = [random.randrange(min_range, max_range) for i in range(n)]
    return list

def neighbor_index_list(list):
    for i in range(len(list)):
        if i % 2 != 0:
            list[i - 1], list[i] = list[i], list[i - 1]
        print(list)


neighbor_index_list(newlist())