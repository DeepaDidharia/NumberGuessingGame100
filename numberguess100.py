import random
import math


n = random.randint(1, 100)
chanceCount = 0
print("Number Guessing Game")
print("Guess a number (between 1 and 100)")

while (chanceCount < 5):

  number = int(input("Enter your number:- "))
  if (n < number):
          print("Your guess is too large: Guess a number less than " ,number)

  elif (n == number):
        print("Congratulation YOU WON !!!!!!")

  elif chanceCount > 5:
    print("You Lose! The the number is ", number)

  else :
    print("Your number guess is too low : Guess a number greater than", number)

   

  chanceCount = chanceCount + 1