import random

n = random.randrange(3,6)

matrixA = [[random.randrange(-100,100) for j in range(n)] for i in range(n)]
matrixB = [[random.randrange(-100,100) for j in range(n)] for i in range(n)]

for listA in matrixA:
    print(listA)

main_diagonal = []
secondary_diagonal = []
for i in range(n):
    if -10 <= matrixA[i][i] <= 10:
        main_diagonal.append(matrixA[i][i])

    secondary_diagonal.append(matrixA[i][n-1-i]) 

if main_diagonal:
    print(f"Элементы главной диагонали удовлетворяющие условию \nМассив: {main_diagonal}")
else:
    print(f"Элементы главной диагонали удовлетворяющих условию не найдено \n" +
          f"Элементы побочной диагонали -> Массив: {secondary_diagonal}")
