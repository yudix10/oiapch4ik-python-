m = float(input("Enter m - "))
n = float(input("Enter n - "))

print(m)
print(n)

if m == n:
    m = 0
    n = 0
else:
    if m < n:
        m = n
    else:
        n = m
print(f'Итог - {m}')
print(f'Итог - {n}')