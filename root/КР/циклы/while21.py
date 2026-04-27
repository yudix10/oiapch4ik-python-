n = int(input('Enter N - '))
counter = 0

while n != 0:
    x = n % 10
    if x % 2 != 0:
        counter += 1
    n //= 10


if counter != 0:
    print(f'Counter - {counter}. TRUE.')
else:
    print(f'Counter - {counter}. FALSE.')

