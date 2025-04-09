from math import sin, cos, sqrt, pi

alf = int(input("Enter alfa: "))

z1 = cos(alf) + sin(alf) + cos(3 * alf) + sin(3 * alf)
z2 = 2 * sqrt(2) * cos(alf) * sin((pi/4) + 2 * alf)

print("__________Result__________")
print("Z1 = " + str(z1) + "\n" + "Z2 = " + str(z2))
print("__________________________")