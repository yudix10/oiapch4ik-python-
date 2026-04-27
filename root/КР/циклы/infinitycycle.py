import math
x = float(input('Enter x - '))
n = int(input('Enter n - '))
rad = math.pi / 4
counter = 1
fc = 1
ans = 1
while n != 0:
    s = math.sin(rad) * x
    ans += s / fc
    rad *= 2
    counter += 1
    fc *= counter
    n -= 1
print(ans)
