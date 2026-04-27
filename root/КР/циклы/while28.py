e = float(input('Enter e - '))
a1 = 2
a2 = 2 + 1/a1 #2,5
k = 2

while abs(a2 - a1) >= e:
    a1 = a2 #2,5
    a2 = 2 + 1/a1 #1,4
    k += 1
print(a1, a2)
print(k)
