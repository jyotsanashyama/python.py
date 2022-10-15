num = int(input("Enter a number: "))
temp1 = num
reverse = 0
while num > 0:
    temp = num%10
    reverse = reverse*10 + temp
    num = num//10


print ("Reverse of the given number: ",reverse)

