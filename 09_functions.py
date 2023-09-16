#Functions 

#Creating a Greeting function
def greeting():
    print("Hi Friend")

def greeting(name):
    print(f"Hi {name}")

#Invoking the function
greeting("Goku")

#Creating a function to sum 2 numbers
def sum(num1, num2):
    total = num1 + num2
    print(f"The Sum of {num1} + {num2} = {total}")

sum(1,2)
sum(156,9678)

#Creating another Greeting function 
def greeting2(name, last_name):
    print(f"Hi {name} {last_name}")

greeting2("Naruto", "Uzumaki")