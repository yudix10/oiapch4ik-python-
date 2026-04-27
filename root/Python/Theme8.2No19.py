from random import randint

#Create matrix
matrix = []
max = 0


n = int(input('Enter row - '))
m = int(input('Enter col - '))
k = int(input('Enter k - '))
count = 0


for i in range(n):
  row = [0] * m
  matrix.append(row)


for i in range(n):
  for j in range(m):
    matrix[i][j] = randint(0, 9)

for i in range(n):
  for j in range(m):
    if matrix[i][j] % k == 0:
      count += 1
      print(matrix[i][j])
    if matrix[i][j] > max:
      max = matrix[i][j]
      


for i in matrix:
  print(*[f"{x:>2}" for x in i])
  

print(f"k - {count}")
print(f"max - {max}")