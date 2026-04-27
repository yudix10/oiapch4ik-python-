n = int(input("Enter number - "))

matrix = []


#Создание матрицы n-ого порядка
for i in range(n):
    row = [0] * n
    matrix.append(row)


for i in range(n):
    for j in range(n - i):
        matrix[i][j] = i + 1


#Вывод массива
for row in matrix:
    print(' '.join(map(str, row)))