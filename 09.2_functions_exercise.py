#Functions: Exercises II

#Creating a Company Bills list
bills = [14,45,65,79,38,137,4,942]

#Creating a Function for showing the bill average. This function will receive the bills list defined above
def media_bill(bills):
    total = sum(bills)
    media = total / len(bills) 
    return media

#Creating a variable to show the result
result = media_bill(bills)
print("The average bill is: ", result)
#Showing result with 2 decimals:
print(f"{result :.2f}")