workingDays = int(input("Write the number of working days: "))
totalDays = int(input("What is the total number of days: "))
percentage = (workingDays/totalDays) *100

if percentage >= 75:
    print("Your attendance is", percentage,"%. You are eligible to give exams.")

else:
    print("Your attendance is only",percentage,"%. Sorry,you are not eligible to give exams.")