import math

k = int(input('Enter k - '))
ans = 1
fc = 1

for i in range(-3, k + 1):
    if i == -2 or i == 9:
        continue
    ans *= (i + 2) * abs(i - 9) / fc
    fc *= i + 4
    print(ans)