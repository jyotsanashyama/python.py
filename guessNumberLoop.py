import random
n = 50
toGuess = int(n*random.random()) + 1 
guess = 0

while guess != toGuess:
    guess = int(input("Enter new number: "))
    if guess > 0:

         if guess > toGuess:
             print("Guessed number is large.Try again!")
         elif guess < toGuess:
             print("Guessed number is small.Try again!")
    else:
        print("Sorry that you are giving up!")
        break
else:
    print("Congratulations! You have guessed it right.")
