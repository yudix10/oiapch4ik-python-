n = int(input())
sum = 1
for i in range(1, n + 1):
    sum *= 1 + i / 10
print(sum)