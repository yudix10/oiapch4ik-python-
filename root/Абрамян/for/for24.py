x = float(input('Enter x - '))
n = int(input('Enter n - '))
zn = -1
a = 1
for i in range(1, n + 1):
    a += zn * a * x * x / ((2*i - 1) * (2 * i))
    zn *= -1
print(a)
