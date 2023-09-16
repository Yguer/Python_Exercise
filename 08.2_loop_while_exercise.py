#Loop While: Exercise - Guess a Number from 1-20
#We will use RANDOM function

import random

print("Welcome to the Game: Guess A Number!")
print("Try to guess a number from 1-20")

#Storing the random number in secret_number variable
secret_number = random.randint(1,20)

#Creating a variable to store guessed number as False
guess = False

#Starting the Loop
while not guess:
    user_guess = int(input("Enter a Number: "))

    if(user_guess == secret_number):
        print("Congratulations you have guessed the Secret Number!")
        guess = True
    elif user_guess < secret_number:
        print("The Secret Number is higher. Try Again!")
    else:
        print("The Secret Number is lower. Try Again!")


