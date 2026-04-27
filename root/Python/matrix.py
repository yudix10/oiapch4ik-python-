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


for i in matrix:
    print(*[f"{x:>2}" for x in i])

for i in  range(0, n):
  for j in range(0, m):
    counter = []
    for k in range(i-1, i+2):
      for l in range(j-1, j+2):
        if k >= 0 and k < n and l >= 0 and l < m:
          if not(k == i and l == j):
            counter.append(matrix[k][l])
            print(counter)
          else:
            continue
    avg = sum(counter) / len(counter)
    new_matrix.append(avg)




print('-----------------------------------')
for i in range(n):
  row = new_matrix[i*m:(i+1)*m]
  print(*[f"{x:>6.2f}" for x in row])