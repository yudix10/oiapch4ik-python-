from random import randint

#Create matrix
matrix = []
new_matrix = []

n = int(input('Enter row - '))
m = int(input('Enter col - '))

for i in range(n):
  row = [0] * m
  matrix.append(row)


for i in range(n):
  for j in range(m):
    matrix[i][j] = randint(0, 9)
    
for k in matrix:
    a = len(k)
    for i in range(0, a - 1):
        for j in range(a - i - 1):
            if k[j] > k[j + 1]:
                k[j], k[j + 1] = k[j + 1], k[j]


for i in matrix:
    print(*[f"{x:>2}" for x in i])