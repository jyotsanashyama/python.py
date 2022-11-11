#Find the factorial of a given number
fact=1
n=int(input("Enter the number upto which you want factorial: "))
for i in range(1,n+1):
    fact=fact*i
print(fact)