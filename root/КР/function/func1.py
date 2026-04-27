import math

start = int(input('Enter start - '))
end = int(input('Enter end - '))
step = 0.2
while start <= end:
    y = start**2 - math.cos(math.pi * start) ** 2
    print(f'x - {"%.1f" % (start)}')
    print(f'y - {"%.2f" % (y)}\n')
    start += step
