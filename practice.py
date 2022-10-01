from tempfile import tempdir
#change the input numbers using third variable

x=input("Enter 1st number:")
y=input("Enter 2nd number:")

temp = x
x =y
y = temp
print("The value of x is:",x)
print("The value of y is:",y) 