#Functions: Exercises

#Show average bill cost from 3 companies

total = 2 + 5 + 7
media = total / 3
print("The Average Bill Cost is: ", media)

#Creating a Function to show average bill cost from 3 companies
def media_bill(bill1, bill2, bill3):
    total = bill1 + bill2 + bill3
    media = total / 3
    print("The Average Bill Cost is: ", media)

media_bill(134, 4567, 9076)

#Creating another Function to show average bill cost from 3 companies
def media_bill(bill1, bill2, bill3):
    total = bill1 + bill2 + bill3
    media = total / 3
    return media

result = media_bill(120, 4560, 944)
print(result)
#Showing result with 2 decimals:
print(f"{result :.2f}")