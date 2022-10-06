#to check wheather the input digit is even or odd:

a=int(input("Enter a digit:"))
if a%2 == 0:
    print(a," is an even number.")
elif a%2!=0:
    print(a," is an odd number.")
else:
    print(a," is neither odd nor even number.")    
