def func(n):
    counter = 0
    for i in range(n, 2 * n + 1):
        for j in range(n, 2 * n + 1):
            if i - j == 2:
                counter += 1
                print(f'i - {i}\nj - {j}\n')

    return counter

print(func(23))