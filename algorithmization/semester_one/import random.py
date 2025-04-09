import random 

def print_matrix(title,matrix):
    print(title)
    for element in matrix:
        print(element) 

n = int(input("Enter the size of the square matrix: "))
matrix =  [[random.randrange(-6, 9) for j in range(n)] for i in range(n)]

print_matrix("Matrix:",matrix)


for i in range(len(matrix)):
    temp = False
    for j in range(len(matrix[i])):
        if abs(matrix[j][i]) == 4:
           temp = True    
    if temp:    
        print(f"Столбец № {i} c элементом равным по модулю с числом 4")       
