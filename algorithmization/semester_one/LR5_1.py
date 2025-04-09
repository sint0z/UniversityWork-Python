import abc

def custom_sum(arr):
    sum = 0
    for elem in arr:
        if elem  < 0 :
            sum += elem
    return sum

def production(arr:list):
    product = 1
    min_elem = max_elem = arr[0]
    i_max, i_min = 0,0
    for i in range(len(arr)):
        if arr[i] < min_elem:
            min_elem = arr[i]
            i_min = i
        elif arr[i] > max_elem:
            max_elem = arr[i]
            i_max = i
            
    if i_max > i_min:
        for k in range(i_min+1, i_max,1):
            product *= arr[k]
        
    if i_min > i_max:
        for k in range(i_max + 1, i_min,1):
            product *= arr[k]

    return product

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)- 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


n = int(input("Enter n: "))
arr = [0] * n

for i in range(len(arr)):
    print("Enter element:" + str(i+1) )
    arr[i] = int(input())

sum = custom_sum(arr)
prod = production(arr)
bubble_sort(arr)

if sum !=0:
    print("Sum =", sum)
else:
    print("There are no negative numbers")
print("Production =", prod)
print("Sorted array:", arr)