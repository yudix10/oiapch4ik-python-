import random
a=[random.randrange(-100,100) for i in range(random.randint(-2,10))]
print(a)
for j in range (len(a)-1,0,-1):
    for i in range (j):
        if a[i]>a[i+1]:
            c = a[i]
            a[i] = a[i+1]
            a[i + 1] = c
print(a)