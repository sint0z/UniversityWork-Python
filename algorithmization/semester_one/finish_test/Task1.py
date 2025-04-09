A = [
    [3,2-5],
    [4,2,0],
    [1,1,2]
    ]

B = [
    [-1,2,4],
    [0,3,2],
    [-1,-3,4]
    ]

M = [[0 for j in range(len(B[i]))] for i in range(len(A))] # Вспомогательная матрица
result = [[0 for j in range(len(B[i]))] for i in range(len(A))] # Вспомогательная матрица

# Действие 1 вычисляем значение (A-B)
for i in range(3):
    for j in range(3):
        M[i][j] = A[i][j] + B[i][j]


for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += M[i][k]*A[k][j]

# (A-B)A+3B
for i in range(len(result)):
    for j in range(len(B[i])):
        result[i][j] += 3 * B[i][j]

# Вывод конечного результата
print("Результирующая матрица (A - B) * A + 3B:")
for row in result:
    print(row)