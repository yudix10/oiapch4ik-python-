from random import randint

#Create matrix
matrix = []
new_matrix = []
summer = 0
n = int(input('Enter row - '))
m = int(input('Enter col - '))

for i in range(n):
  row = [0] * m
  matrix.append(row)

for i in range(n):
  row = [0] * m
  new_matrix.append(row)

for i in range(n):
  for j in range(m):
    matrix[i][j] = randint(0, 9)

for row in matrix:
    print("".join(f"{el:4}" for el in row))

for i in  range(0, n):
  for j in range(0, m):
    counter = []
    for k in range(i-1, i+2):
      for l in range(j-1, j+2):
        if k >= 0 and k < n and l >= 0 and l < m:
          if not(k == i and l == j):
            result = matrix[k][l]
            counter.append(round(result, 1))
            print(counter)
          else:
            continue
    avg = sum(counter) / len(counter)
    new_matrix[i][j] += avg

print('------------------------------------------------------------------')
for i in range(len(new_matrix)):
    for j in range(len(new_matrix)):
        print("{:6.2f}". format(new_matrix[i][j]), end='')
    print()


for i in range(0, n):
    for j in range(0, m):
        summer += new_matrix[i][j]

print('------------------------------------------------------------------')
print(summer)