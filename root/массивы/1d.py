n = int(input("Enter number - "))

matrix = []


#Создание матрицы n-ого порядка
for i in range(n):
    row = [0] * n
    matrix.append(row)


for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            matrix[i][j] += 1
        else:
            continue


#Вывод массива
for row in matrix:
    print(' '.join(map(str, row)))