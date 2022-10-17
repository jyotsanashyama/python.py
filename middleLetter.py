#take input of name, print 1st and last letter of name

name = str(input("Enter your name:"))
print("First letter:",name[0])
print("Last letter:",name[-1])
length = len(name)
print(length)

if length%2!=0:#for odd
    mid = int((length+1)/2)
    print("Middle letter:",name[mid-1])
elif length%2 == 0:#for even
    mid1 = int(length/2)
    mid2 = int((length/2)+1)
    print("Middle letter:",name[mid1-1],"and",name[mid2-1])

