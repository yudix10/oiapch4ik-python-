x = float(input('Enter x - '))
n = int(input('Enter n - '))
zn = 1
a = x
b = 1
sum = x
for i in range(1, n + 1):
    zn *= -1
    a = a * x * x
    b = zn * a / (2 * n + 1)
    sum += b
print(sum)
