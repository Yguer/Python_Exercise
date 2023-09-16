#Genearal Exercises

#Exercise 1: Create a Multiplication Table. User will enter the number manually.
#Creating a function to multiply
def mult_table(table, limit):
    for i in range(1,limit):
        result = table * i
        print(f"{table} x {i} = {result}")

#Asking user input
table = int(input("Which Multiplication Table do you want to learn? "))

#Showing the Multiplication Table:
mult_table(table,11)


#Exercise 2: Same as above but defining the limit in the range
#Creating a function to multiply
def mult_table(table):
    for i in range(1,16):
        result = table * i
        print(f"{table} x {i} = {result}")

#Asking user input
table = int(input("Which Multiplication Table do you want to learn? "))

#Showing the Multiplication Table:
mult_table(table)