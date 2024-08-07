print("Welcome to Ansh's Snacking Station!")
print("What would you like to order?")
print("Options:")
print("Type \"1\" for Veg Burger: $4.59")
print("Type \"2\" for Grilled Sandwich: $3.99")
print("Type \"3\" for French Fries: $2.49")
print("Type \"4\" for Spaghetti: $3.99")

opted = int(input("Type your option below:\n"))
bill = 0.00

if opted == 1:
    bill += 4.59
    cheese = input("Want extra cheese? +$0.50\n Type \"Y\" for Yes and \"N\" for no.\n")
    if cheese == "Y" or cheese == "y":
        bill += 0.50
elif opted == 2:
    bill = 3.99
    jalapeno = input("Add Jalapeno? +$0.25\n Type \"Y\" for Yes and \"N\" for no.\n")
    if jalapeno == "Y" or jalapeno == "y":
        bill += 0.25
elif opted == 3:
    bill = 2.49
elif opted == 4:
    bill = 3.99
    sauce = input("Add Marinara Sauce? +$0.55\n Type \"Y\" for Yes and \"N\"for no.\n")
    if sauce == "Y" or sauce == "y":
        bill += 0.55
coke = input("Would you like to add a refreshing Coke? +$1.00\n Type \"Y\" for  Yes and \"N\" for no.\n")
if coke == "Y" or coke == "y":
    bill += 1.00
latte = input("Would you like to add an Iced Latte?? +$1.50\n Type \"Y\" for  Yes and \"N\" for no.\n")
if latte == "Y" or latte == "y":
    bill += 1.50
print(f"Your final bill amount is: ${bill}")
print("Thank you for choosing Ansh's Snacking Staion!")
input("Press enter to close.")