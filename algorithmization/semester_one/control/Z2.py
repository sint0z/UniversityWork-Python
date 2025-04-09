import random

def print_matrix(title,matrix):
    print(title)
    for element in matrix:
        print(element) 

n = int(input("Введите кол-во рядов: "))
m = int(input("Введите кол-во сидений в ряду: "))

matrix = [[random.randint(0,1) for j in range(m)] for i in range(n)]
print_matrix("Концертный зал:",matrix)

r = 0
m1 = 0
m2 = 0

for i in range(n):
    temp = matrix[i][0]
    isCheck = False
    for j in range(1,m):
            if temp == matrix[i][j] and temp !=1 and matrix[i][j] != 1:
                r = i+1
                m1,m2 = j,j+1
                isCheck = True
                break
            else:
                temp = matrix[i][j]
    if isCheck : 
         break                
    
if r > 0:
     print(f"Свободные места в ряду {r} -  места {m1}{m2}")
else:
     print("Свободных мест нет")