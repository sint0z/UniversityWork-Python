import random

def print_matrix(title,matrix):
    print(title)
    for element in matrix:
        print(element) 

matrix = lambda m,p: [[random.randrange(-6, 9) for j in range(p)] for i in range(m)]

row_matrixA = int(input("Введите кол-во строк в матрице A:"))
col_matrixA = int(input("Введите кол-во столбцов в матрице A:"))

row_matrixB = int(input("Введите кол-во строк в матрице B:"))
col_matrixB = int(input("Введите кол-во столбцов в матрице B:"))

matrixA = matrix(row_matrixA,col_matrixA)
print_matrix("Матрица А", matrixA)
matrixB = matrix(row_matrixB,col_matrixB)
print_matrix("Матрица B", matrixB)

if col_matrixA != row_matrixB:
    print(f"Матрицук А невозможно умножить на матрицу В ({col_matrixA} не равно {row_matrixB})")
else:
    result_matrix = [[0 for j in range(col_matrixB)] for i in range(row_matrixA)]
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
               result_matrix[i][j] += matrixA[i][k]*matrixB[k][j]

print_matrix("Результат умножения матриц", result_matrix)
               


