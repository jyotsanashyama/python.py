age1 = int(input("Please enter your age Person1: "))
age2 = int(input("Please enter your age Person2: "))
age3 = int(input("Please enter your age Person3: "))

if age1 > age2 and age1 >age3 and age2 > age3:
    print("Person1 is the oldest and Person3 is the youngest.")

elif age1 > age2 and age1> age3 and age2 < age3:
    print("Person1 is the oldest and Person2 is the youngest.")

elif age1 == age2 and age2 > age3:
    print("Person3 is the youngest and rest have the same age.")

elif age1 == age2 and age2 < age3:
    print("Person3 is the oldest and rest have same age.")

elif age1 == age3 and age2 > age3:
    print("Person2 is the oldest and rest have the same age.")

elif age1 == age3 and age2 < age3:
    print("Person2 is the youngest and rest have the same age.")

elif age2 == age3 and age1 > age2:
    print("Person1 is the oldest and rest have the same age.")

elif age2 == age3 and age1 < age2:
    print("Person1 is the youngest and rest have the same age.")

elif age2 > age3 and age2 > age1 and age1 > age3:
    print("Person2 is the oldest and Person3 is the youngest.")

elif age2 > age3 and age2 > age1 and age1 < age3:
    print("Person2 is the oldest and Person1 is the youngest.") 

elif age3 > age1 and age3 > age2 and age1 > age2:
    print("Person3 is the oldeset and Person2 is the youngest.")

elif age3 > age1 and age3 > age2 and age1 < age2:
    print("Person3 is the oldest and Person1 is the smallest.")

else:
    print("All people have the same age.")





