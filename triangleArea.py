import math
a = float(input("Enter 1st side of triangle:"))
b = float(input("Enter 2nd side of triangle:"))
c = float(input("Enter 3rd side of triangle:"))
s = (a+b+c)/2 #semiperimeter of triangle
#area of triangle = sqrt (s(s-a)(s-b)(s-c))
x = s - a
y = s - b
z = s - c
m = x*y*z
area = math.sqrt(s * m)
print("Area of triangle is:", area)
