def list():
    list = []
    n = int(input('Enter number - '))
    for i in range(n):
        k = float(input('Enter number in list - '))
        list.append(k)
    return list

def func(list):
    k = int(input('Enter k - '))
    sum = 0
    for i in list:
        if i % k == 0:
            sum += i
    return sum

list1 = [1, 2, 3, 4, 5]

print(func(list()))