#Write a program to display all prime numbers within a range
#Take the user input for start and end of range.
start=int(input("Enter the starting range: "))
end=int(input("Enter the ending range: "))
for number in range(start,end+1):
    if number>1:
        for i in range(2,number):

            if number%i==0:
                break
        else:
            print(number)
       
      
   
   
   
    