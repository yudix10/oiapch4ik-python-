n = int(input())

zero = 1

while n != 0:
    print((n % 10) * zero)
    n = n // 10
    zero *= 10