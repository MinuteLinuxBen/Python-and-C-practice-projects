# Benjamin Smith
# 2/14/2022

# The purpose of this program is to guide a person interested in buying a car with yes or no questions.
# This can be represented as True/False (1/0 Bool lean values).
# The program has categories for cars that can be selected and elifs represent their choices.

# Define the main fucntion

# Define and intialize variables and strings.
# Declare constants.
# Display an introduction.
# ASCII or regular introduction text.
# Prompt the user for a name.
# Prompt the user for an age.
# If the user is under the age of 16 the program will stop and the user cannot go any further.
# If the user is 16 or older they may proceed into the program.
# Prompt the user for a car choice use an A-D selection method for the category of car.
# Once the car type is selected display the features including the name and specifactions of the vehicle.
# Once the user picks the vehicle type they are taken to a check out where they are asked if they want.
# a year of oil changes, general maintenance, or road side assistance.
# Calculate sales tax from the total cost of car (car_type * 7% sales_tax).
# Calculate fees for oil changes (Car_Type_With_Sales_Tax + oil_change).
# Calculate fees for general maintenance (Car_Type_With_Sales_Tax + general_maintance).
# Calculate fees for road side assitance (Car_Type_With_Sales_Tax + road_side).
# Display sales tax, Price for oil changes, and general maintenance, or road side assitance. Sales tax is automatically included at check out.
# Once they pick a car and service they have successfully bought a car with "Prestige Auto".
# congratulate them and display a thank you message at the end of the program.

# Call main function


#Constants for cars
Sedan=20000
Truck=25000
SUV=30000
#Eletric vehicle(EV)
EV=32000

#Constants for service
oil_change=150
general_maintance=200
road_side=175
under_age=15

#Salestax constant with 1 in front of the decimal place
sales_tax = 1.07

#String names
name="".capitalize()
#Vehicle name choices A-D
Sedan_choice="A".lower()
Truck_choice="B".lower()
SUV_choice="C".lower()
EV_choice="D".lower()

#Define main function
#Proceed to prompt user for name and age.
def main():
    print("Welcome to Prestige Auto Sales")
    print("-"*40)
    name = input("Please enter your name: ").capitalize()
    age = int(input("Please enter your legal age:"))
    if age <= under_age:
         print(f"User: {name}, is under age and may not proceed.")
         exit()
    else:
        print("please choose from one of the car categories:")

    #Prompt the user with a list of cars in a (A-D) selection style
    car_choice= input("(A) Sedan  (B) Truck  (C) SUV  (D) EV\n").capitalize()
    if car_choice == "A":
        print("\nBrand: Nissan  Model: Sentra  Year:  2022  Engine type: 4-cylinder  Transmission type: CVT")
        print("Price: $20,000")
    elif car_choice == "B":
        print("\nBrand: Dodge   Model: Dakota  Year: 1996   Engine type: 6-cylinder  Transmission type: 4-speed automatic")
        print("Price: $25,000")
    elif car_choice == "C":
        print("\nBrand: Dodge   Model: Durango  Year: 2020  Engine type: 8-cylinder  Transmission type: 8-speed automatic")
        print("Price: $30,000")
    elif car_choice == "D":
        print("\nBrand: Tesla  Model: Y\tYear: 2021 Motor type: Permanent Magnet Synchronous Reluctance Motor Transmission type: 1-speed automatic")
        print("Price: $32,000")
    else:
        print("Error... Must select a leter (A-D) in our catalog of choices.")

    #Basic calculations for services and sales tax
    import math
    #sales tax with the cost of the car
    sedan_taxed=(Sedan*sales_tax)
    truck_taxed=(Truck*sales_tax)
    SUV_taxed=(SUV*sales_tax)
    EV_taxed=(EV*sales_tax)
    
    #oil change and car
    sedan_oiled=(Sedan * sales_tax + oil_change)
    truck_oiled=(Truck * sales_tax + oil_change)
    SUV_oiled=(SUV * sales_tax + oil_change )

    #Roadside and car
    sedan_road=(Sedan * sales_tax + road_side)
    truck_road=(Truck * sales_tax + road_side)
    SUV_road=(SUV * sales_tax + road_side)
    EV_road=(EV * sales_tax + road_side)

    #maintenace and car
    sedan_maint=(Sedan * sales_tax + general_maintance)
    truck_maint=(Truck * sales_tax + general_maintance)
    SUV_maint=(SUV * sales_tax + general_maintance)
    EV_maint=(EV * sales_tax + general_maintance)
#############################################################################
    print("-"*40)
#############################################################################
    print("would you like to include one year of oil changes maintenance for $150?")
    print("Note: Electric vehicles do not require routine oil changes.")
    oil = input("(Y/N)\n ").capitalize()
    if oil == "Y":
        print("Charges won't be reflected until checkout...")
    elif oil == "N":
        print("You have selected (N) and this option is voided")
    else:
        print("Error... User may only select (Y/N) to proceed.\n")
###########################################################################
    print("-"*40)
###########################################################################
    print("\nwould you like to include one year of general maintenance for $200?")
    mainty = input(" (Y/N)\n ").capitalize()
    if mainty == "Y":
        print("")
    elif mainty == "N":
        print("You have selected (N) and this option is voided")
    else:
        print("Error... User may only select (Y/N) to proceed.\n")
##########################################################################
    print("-"*40) 
##########################################################################
    print("\nwould you like to include one year of roadside assistance for $175?")
    road = input(" (Y/N)\n ").capitalize()
    if road == "Y":
        print("")
    elif maint == "N":
        print("You have selected (N) and this option is voided")
    else:
        print("Error... User may only select (Y/N) to proceed.\n")
##########################################################################
    print("-"*40) 
##########################################################################
    if car_choice == "A":  
        print (f"Sedan with 7% sales tax: $ {sedan_taxed}.")
    elif car_choice == "B":
        print (f"Truck with 7% sales tax: $ {truck_taxed}.")
    elif car_choice == "C":
        print (f"SUV with 7% sales tax: $ {SUV_taxed}.")
    elif car_choice == "D":
        print (f"EV with 7% sales tax: $ {EV_taxed}.")
    else:
        print("Error... Something went wrong with the selection process.\n")

#Sedan with options picked
##########################################################################
    print("-"*40) 
##########################################################################
    #Car and the price of oil changes at the checkout
    if car_choice == "A" and oil == "Y":
        print(f"Sedan with 1-year of oil changes: $ {sedan_oiled}")
    elif car_choice == "A" and oil == "N":
        print(f"Sedan without oil changes: $ {sedan_taxed}.")
    else:
        print("")

    if car_choice =="A" and mainty =="Y":
        print(f"Sedan with 1-year of general maintenance: $ {sedan_maint}.")
    elif car_choice == "A" and mainty == "N":
        print(f"Sedan without general maintenance: $ {sedan_taxed}.")
    else:
        print("")

    if car_choice =="A" and road =="Y":
        print(f"Sedan with 1-year of roadside assistance: $ {sedan_road}.")
    elif car_choice == "A" and road == "N":
        print(f"Sedan without roadside assistance: $ {sedan_taxed}.")
    else:
        print("")
##########################################################################
    print("-"*40) 
##########################################################################

#truck with options picked
##########################################################################
    print("-"*40) 
##########################################################################
    #Car and the price of oil changes at the checkout
    if car_choice == "B" and oil == "Y":
        print(f"Truck with 1-year of oil changes: $ {truck_oiled}")
    elif car_choice == "B" and oil == "N":
        print(f"Truck without oil changes: $ {truck_taxed}.")
    else:
        print("")
        
    if car_choice =="B" and mainty =="Y":
        print(f"Truck with 1-year of general maintenance: $ {truck_maint}.")
    elif car_choice == "B" and mainty == "N":
        print(f"Truck without general maintenance: $ {truck_taxed}.")
    else:
        print("")

    if car_choice =="B" and road =="Y":
        print(f"Truck with 1-year of roadside assistance: $ {truck_road}.")
    elif car_choice == "B" and road == "N":
        print(f"Truck without roadside assistance: $ {truck_taxed}.")
    else:
        print("")
##########################################################################
    print("-"*40) 
##########################################################################

   #SUV with options picked
##########################################################################
    print("-"*40) 
##########################################################################
    #Car and the price of oil changes at the checkout
    if car_choice == "C" and oil == "Y":
        print(f"SUV with 1-year of oil changes: $ {SUV_oiled}")
    elif car_choice == "C" and oil == "N":
        print(f"SUV without oil changes: $ {SUV_taxed}.")
    else:
        print("")

    if car_choice =="C" and mainty =="Y":
        print(f"SUV with 1-year of general maintenance: $ {SUV_maint}.")
    elif car_choice == "C" and mainty == "N":
        print(f"SUV without general maintenance: $ {SUV_taxed}.")
    else:
        print("")

    if car_choice =="C" and road =="Y":
        print(f"SUV with 1-year of roadside assistance: $ {SUV_road}.")
    elif car_choice == "C" and road == "N":
        print(f"SUV without roadside assistance: $ {SUV_taxed}.")
    else:
        print("")
##########################################################################
    print("-"*40) 
########################################################################## 


   #EV with options picked
##########################################################################
    print("-"*40) 
##########################################################################
    #Car and the price of oil changes at the checkout
    if car_choice == "D" and oil == "Y":
        print("Electric vehicles do not need engine oil. Your amount will be reflected by $0")
    elif car_choice == "D" and oil == "N":
        print(f"Regular price of EV: $ {EV_taxed}.")
    else:
        print("")

    if car_choice =="D" and mainty =="Y":
        print(f"EV with 1-year of general maintenance: $ {EV_maint}.")
    elif car_choice == "D" and mainty == "N":
        print(f"EV without general maintenance: $ {EV_taxed}.")
    else:
        print("")

    if car_choice =="D" and road =="Y":
        print(f"EV with 1-year of roadside assistance: $ {EV_road}.")
    elif car_choice == "D" and road == "N":
        print(f"EV without roadside assistance: $ {EV_taxed}.")
    else:
        print("")
##########################################################################
    print("-"*40) 
########################################################################## 
    print(" Fantastic! You are now the happy owner of a proudly selected car!")
    print(" Thank you so much for using Prestige Auto sales!")

    
main()






