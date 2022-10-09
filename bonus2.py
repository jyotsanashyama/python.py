salary = int(input("What is your salary?"))
yearsOfWork = int(input("Enter your years of work in this company: "))

if yearsOfWork >= 10:
    bonus = (10/100)*salary
    print("Congratulations! Your bonus is ",bonus,"and your new salary is ",salary + bonus)

elif yearsOfWork > 6 and yearsOfWork < 10:
    bonus = (8/100)*salary
    print("Congratulations! Your bonus is ",bonus,"and your new salary is ",salary + bonus)


elif yearsOfWork <= 6 and yearsOfWork > 0:
    bonus = (5/100)*salary
    print("Congratulations! Your bonus is ",bonus,"and your new salary is ",salary + bonus)

else:
    print("Sorry, you will not get any bonus.")