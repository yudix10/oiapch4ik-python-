import random

def CreateMatrix(n, m):
    matrix = []

    for i in range(n):
        row = [0] * m
        matrix.append(row)

    for i in range(n):
        for j in range(m):
            matrix[i][j] = random.randint(1,100)
    return matrix


def PrintMatrix(matrix):
    for i in matrix:
        print(*i)

def algoritm(matrix):
    k = 0
    sum = 0

#Сумма первого столбца
    for i in range(0, len(matrix) + 1):
        for j in range(0, len(matrix)):
            print(matrix[j][i])


    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if j != 0:
                if matrix[i][j] > sum:
                    k += 1



    PrintMatrix(matrix)
    print(sum)
    print(k)


print(algoritm(CreateMatrix(8,4)))