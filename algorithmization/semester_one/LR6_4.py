import random
import math

def print_matrix(title,matrix):
    print(title)
    for element in matrix:
        print(element) 

def product_non_negative_row(matrix):
    prod = 1
    len_matrix = len(matrix)
    
    for i in range(len_matrix):
        is_negative = False
        for j in range(len_matrix):
            if matrix[i][j] < 0:
                is_negative = True
                
        if not is_negative:
            prod *=  matrix[i][j]
            
    return prod

def max_diagonal_sum(matrix:list):
    max_sum = 0
    
    for i in range(1,len(matrix)-1):
        temp_sum1 = 0 
        temp_sum2 = 0 
        for j in range(len(matrix) - i):
            temp_sum1 += matrix[j][i+j]
            temp_sum2 += matrix[i+j][j]
    if temp_sum1 > max_sum:
        max_sum = temp_sum1
    if temp_sum2 > max_sum:
        max_sum = temp_sum2
    return max_sum

n = int(input("Enter the size of the square matrix: "))
matrix =  [[random.randrange(-6, 9) for j in range(n)] for i in range(n)]

temp = 0
for i in range(n-1):
    for j in range(n-1):
        if matrix[j][i] == 4:
            print(i,j)
            temp = i
    print(f"Столбец № {temp+1} c элементом равным по модулю с числом 4")       


print_matrix("Matrix:",matrix)
prod = product_non_negative_row(matrix)
sum = max_diagonal_sum(matrix)

print("The product in rows that do not count:",prod)
print("Max sum diagonal:",sum)