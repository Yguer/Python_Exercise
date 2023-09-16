#Loop While: Exercise - Guess a Number from 1-5
#We will use RANDOM function

import random

print("Welcome to the Game: Guess A Number!")
print("Try to guess a number from 1-5")

#Storing the random number in secret_number variable
secret_number = random.randint(1,5)

#Creating a variable to store guessed number as False
guess = False

#Starting the Loop
while not guess:
    user_guess = int(input("Enter a Number: "))

    if(user_guess == secret_number):
        print("Congratulations you have guessed the Secret Number!")
        guess = True
