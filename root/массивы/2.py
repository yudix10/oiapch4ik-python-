n = int(input("Enter number - "))

matrix = []


#Создание матрицы n-ого порядка
for i in range(n * 2):
    row = [0] * n * 2
    matrix.append(row)

for i in range(2 * n):
    for j in range(2 * n):
        if


#Вывод массива
for row in matrix:
    print(' '.join(map(str, row)))