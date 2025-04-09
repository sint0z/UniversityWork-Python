num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1 += num2
num2 = num1 - num2
num1 = num1 - num2

print("__________Result__________")
print("number one = " +  str(num1) + "\n" + "number two =" + str(num2))
print("__________________________")