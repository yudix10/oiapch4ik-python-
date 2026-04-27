n = int(input("Enter number - "))

matrix = []


#Создание матрицы n-ого порядка
for i in range(n):
    row = [0] * n
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            matrix[i][j] = j + 1
        else:
            matrix[i][j] = n - j



#Вывод массива
for row in matrix:
    print(' '.join(map(str, row)))