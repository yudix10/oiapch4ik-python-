matrix = []

n = int(input('Enter row - '))
m = int(input('Enter col - '))

for i in range(n):
  row = [0] * m
  matrix.append(row)



for i in range(0, n):
  count = 0
  for j in range(0, m):
    if i <= j:
      count += 1
      matrix[i][j] += count

for i in matrix:
    print(*[f"{x:>2}" for x in i])