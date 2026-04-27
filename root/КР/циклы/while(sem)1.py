n = int(input())
sum = n % 10

while n > 10:
    n = n // 10
print(n + sum)