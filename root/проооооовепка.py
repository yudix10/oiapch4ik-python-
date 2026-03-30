import random
a=[random.randrange(-100,100) for i in range(random.randint(-2,10))]
print(a)
for j in range (len(a)-1,0,-1):
    max=a[0]
    k=0
    for i in range (0,j+1):
        if a[i]< max:
            max = a[i]
            k=i
    a[k] = a[j]
    a[j] = max
print(a)
