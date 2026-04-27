from random import randint

matrix = []

#Создание массива
n = int(input("Enter number - "))

for i in range(n):
    row = [0] * n
    matrix.append(row)

sum = 0
c = 0

for i in range(n):
    for j in range(n):
        counter = 0
        matrix[i][j] = randint(1, 9)
        if i < j:
            sum += matrix[i][j]
            c += 1
print(sum, c)

#Вывод массива
for row in matrix:
    print(*row)