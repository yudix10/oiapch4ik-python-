import random
def func(x, y):
    while True:
        A = 0
        if (x <= 19) or (y < 2 * x + A - 50) or (y > 17):
            return A
        else:
            x = random.randint()
            y = random.randint()
            A += 1

print(func(1, 18))