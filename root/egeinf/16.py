def func(n):
    if n > 400:
        return n
    else:
        return n + 6 + func(n + 12)

print(func(72))

#1 - 7128
#2 - 6858
print(7128-6858)
#270