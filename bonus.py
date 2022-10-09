yearsOfWorking = int(input("Enter your year of service: "))
salary = float(input("What is your salary? "))

if yearsOfWorking > 5:
    newSalary = salary + 1000 #bonus salary = 1000Rs
    print (" Your new salary is ",newSalary)
else:
    print ("Oops!You will not get any bonus.Your salary is ",salary)
