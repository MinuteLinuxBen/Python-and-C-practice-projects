##############################################################################
# Benjamin Smith
# March 12, 2022
# Snack Bar Menu program.py
# Define the function for each section of the program
# e.g. def intro() and def menu()
# Declare and intialize all constants and variables
# Display a nice introduction with text or ASCII font.
# The greeting is spaced with the sleep function (1)
# The purpose is to catch the viewer's eye with the first word
# for the first half of the establishment's name "Gonzo".
# Display borders and line seperations to make the program
# appear neat and together
# Define the menu section of the program
# Display a menu featuring four menu items sold in "Gonzo Pub".
# Begin with a while loop, so the user can return to the menu again and again
# make the loop=1 so the program can continue and not terminate after one choice
# To make things smoother add a the "except" function to keep a user from
# adding a float or number with decimals
# The while loop is accompanied with a nested function. This allows the user
# to pick all [5] choices in the menu structure.
# The total is kept running from the constants adding each time the
# user selects an item number.
# The user understands that selecting[5] with close the program and display
# the total accumulated as the program continued.
# Most importantly the else statement is another prevention to keep the user
# from selecting a number outside of 1 or 5 as an option.
# Upon closing the program a message to thank the patron will appear.
################################################################################
#Declare constants and intialize possible variables
Scorpion_Price=10.00
Chickens_Price=12.00
Frog_Curry=14.00
Alligator_Price=16.00
Running_total=0.0
Tax=7.0
# Define the function for intro()
def intro():
    print("~"*24)

Gonzo=("""

    _____                       
  / ____|                      
 | |  __  ___  _ __  _______   
 | | |_ |/ _ \| '_ \|_  / _ \  
 | |__| | (_) | | | |/ / (_) | 
  \_____|\___/|_| |_/___\___/  
                               
                        


""")
# Print the  title in half using the time function.
print(Gonzo)
import time
time.sleep(1)

Pub=("""

  _____       _     
 |  __ \     | |    
 | |__) |   _| |__  
 |  ___/ | | | '_ \ 
 | |   | |_| | |_) |
 |_|    \__,_|_.__/ 
                    
                    
                    
                    
                       

""")
print(Pub)
print("\n")
print("-"*24)
print("Menu/Pricing")
print("-"*24)
intro()

# define the menu()
def menu():
    print()
# Begin with a while loop and create the loop to = 1 so the program continues in execution.
loop = 1
while loop == 1:
    print("[1] Scorpion Kebab   $10.00")
    print("[2] Chicken's feet   $12.00")
    print("[3] Frog curry       $14.00")
    print("[4] Alligator fillet $16.00")
    print("[5] Exit")
    print("-"*24)
    # Use a nested selection structure in the while loop, so options selected are accounted for, and the running total is kept.
    # When the user is completed with ordering from the menu they may close the program at any time with the [5] option.
    # Try function allows the user to pick a constant number from the menu.
    # Except function is an added way of keeping the user from adding any choices with extra decimals.
    # Else closes any errors missed, as the user may enter a negative number or anything greater than [5].
    # The last option will close the program and display a "thank you" message, because the business was supported by the patron.
    try:
        option=int(input("Enter menu item number: "))
        print("-"*24)
    except ValueError:
        print("Choice must be a whole number.")
        print("-"*24)
        continue
    if option == 1: 
        Running_total+=Scorpion_Price
        print("Current Total: $"+str(Running_total));
    elif option == 2:
        Running_total+=Chickens_Price
        print("Current Total: $"+str(Running_total));
    elif option == 3:
        Running_total+=Alligator_Price
        print("Current Total: $"+str(Running_total));
    elif option == 4: 
        Running_total+=Frog_Curry
        print("Current Total: $"+str(Running_total));
    elif option == 5:
        print("Current Food Bill: $"+str(Running_total));
        sales_tax=Running_total*Tax/100
        print("Local Sales Tax: $"+str(sales_tax));
        print("Total Bill: $"+str(Running_total+sales_tax))
        import time
        time.sleep(2)
        print("-"*24)
        print("Thank you for dining in with us!")
        exit()
    else:
        option <1 or option >5
        print("The choice made is invalid. Please pick a number choice 1 - 5.")
menu()


