#take str input, if len > 3 char... add ing as (in last) else, print input 
string = str(input("Enter your name:"))
length = len(string)
print(length)

if length > 3:
    new = string + "ing"
    print(new)

else:
    print(string)