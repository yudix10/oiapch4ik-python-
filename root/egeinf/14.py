n = 4 ** 644 + 4 ** 322 + 4 ** 70 - 4 ** 9

counter = 0
while n > 0:
    digit = n % 4
    if digit == 3:
        counter += 1
    n //= 4

print(counter)

#61