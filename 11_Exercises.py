#Genearal Exercises II

#Exercise 1: Calculating the total price of a purchase.
#You work in a shop store and you need to create a program for calculating the total price for a purchase
#Including the tax (7%)
#The user will enter the name of the product, the quantity and the unit price
#The program will calculate the final price and will show a sumary for that purchase


#Creating a function to calculate the Total Price
def calculate_total_price(qty, unit_price):
        #Calculating Total Price
        total_price = qty * unit_price
        return total_price

#Creating a Main function
def main():
     print("Welcome to your Virtual Shop")
     product = input("Enter the Product Name: ")
     qty = int(input("Enter the Quantity: "))
     unit_price = float(input("Enter the Unit Price: "))

     #Validating User inputs:
     if qty <= 0 or unit_price <= 0:
        print("Input Can't be less than 1")
     else:
        total_price = calculate_total_price(qty,unit_price)
        #Calculating tax
        tax = total_price * 0.07
        #Calculating Final Price
        final_price = total_price + tax

        #Showing Data on Screen:
        print("SUMMARY PURCHASE")
        print(f"Product: {product}")
        print(f"Quantity: {qty}")
        print(f"Unit Price: ${unit_price:.2f}")
        print(f"Total: ${total_price:.2f}")
        print(f"Tax (7%): ${tax:.2f}")
        print(f"Total: ${final_price:.2f}")
        print("Thank You!")

#Invoking Main function
main()
