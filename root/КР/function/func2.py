import math
start = float(input('Enter x - '))
end = float(input('Enter n - '))
while start <= end:
    func1 = 1
    func2 = 1
    func3 = 1
    if start > 4:
        func1 = math.sqrt(math.tan(start**2 - 1))
        print('%.2f' % (func1))
    elif 0 <= start <= 4:
        func2 = - 2 * start
        print('%.2f' % (func2))
    elif start < 0:
        func3 = math.e ** math.cos(start)
        print('%.2f' % (func3))
    start += 0.2