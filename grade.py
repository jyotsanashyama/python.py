marks = int(input("Enter your marks: "))

if marks>90 and marks<=100:
    print("Your grade is: A")

elif marks>80 and marks<=90:
    print("Your grade is: B")

elif marks>70 and marks<=80:
    print("Your grade is: C")

elif marks<70 and marks>=0:
    print("Your grade is: D")
else:
    print("Enter your marks between 0 to 100")
