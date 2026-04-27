import random
def newlist():
    n = int(input('Enter number elements in list - '))
    min_range = int(input('Enter min range in list - '))
    max_range = int(input('Enter max range in list - '))
    list = [random.randrange(min_range, max_range) for i in range(n)]
    return list


def bubble_sort(list):
    print(list)
    for i in range(len(list)):
        for j in range(1, len(list)):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
    return list

print(bubble_sort(newlist()))