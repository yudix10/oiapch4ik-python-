counter = 0
ticket = 999999
for i in range(ticket + 1):
    sum = 0
    while i != 0:
        sum += i % 10
        i //= 10
        if sum == 26:
            print(i)
            counter += 1

print(counter)