n = int(input('Enter n - '))
i = 1
counter = 0

while (counter <= 2) and (n >= i):
    if n % i == 0:
        counter += 1
    i += 1

print(counter)
print(i - 1)
if counter == 2:
        print(f'Число {n} простое.')
else:
    print(f'Число {n} составное.')