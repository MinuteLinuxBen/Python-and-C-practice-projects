# Benjamin Smith
# February 14, 2022
# The purpose of this program is to determine the type of vehicle a customer wants rent.
# This is accomplished by prompting them with questions and the alogrithm matching their requests with elifs statements.
# Define the main function.
# Create and use constants.
# Define and intialize varibles.
# The car type is reflected as a constant because vehicle choice remains the same depending on the choices listed from the user.
# Display the intro
# The title "Prestige Auto Rental" can be display normally or with a unique ascii font style.
# The logo for "Prestige Auto Rental" can be created with the Python Turtle drawing function.
# Prompt the user for a first and last name.
# Prompt the user for an age.
# Inform the user the legal age to drive one of their rental cars.
# In this case the user must be the age 16 or older to operate one of their cars.
# If the user is under the age of 16 they won't be allowed to continue with the rental process.
# Ask the user the type of car they would like to rent. Options: Economy, Compact, SUV, Truck.
# Ask the user if they have been in a maximum of three car accidents. If they exceed this limit they don't qualify for a plan (Y/N Question)
# If yes then an error will inform the user that they do not qualify for a rental.
# Ask the user if the would like insurance. In this case Insurance is a flat rate. Optionally charge higher or lower rates depending on car type (Y/N Question).
# Ask the user how many passengers will be in the car. (Y/N Question).
# Ask the user how many drivers will be operating the car. Depending on answer the insurance purchased is only good for "Driver#1" If two drivers are using the car.
# Display an optional charge for the other driver of the car in this case "Driver#2".
# If no then make another suggestion. But, be sure this is optional. 
# Calculate the cost of a rental car depending on the type choosen. Economy, Compact, SUV, Truck.
# Calculate the type of car chosen multiplied by the rates for 1 day, 1 week, 1 month, and 3 months. The time for rental is fixed making the four choices a constant.
# Calculate the costs of insurance stacked onto the cost of the vechicle.
# Calulate any additional insurance need if anyone else driving exceeds "Driver#1."
# Passengers do not have a cap limit as long as everyone can fit within the car. The number of passengers tells the user a better option for a car they should use from passenger count.
# Display the user's first and last name along with age
# Display the cost of all vehicle options
# Display if the user is under the age of 16 the message "Must be 16 or older to drive/rent a vehicle."
# Display an error message instructing the user that they do not meet the age requirements
# Display The question "Have you exceeded more than 3 accidents on your driving record."
# Display to the user an error message " Based off of your driving record you exceed our terms and limits to rent a car."
# Display the question "Would you like to tag on insurance in case of an accident or property damage?"
# Diplay the message "Our insurance plan offers complete coverage. By selecting yes you have agreed to be liable for all damages associated with this rental."
# Display The question "How many drivers will be operating this vehicle?"
# Display the question "How many passengers will be riding in your chosen vehicle?"
# Display the quote back for every option picked by the user.
# Display a message thanking the user for using "Prestige Auto Rental!"

# Call the main function

def main():
    #Create Constants
    
    Economy_Cost = 50
    Compact_SUV_Cost = 60
    SUV_Cost = 100
    Truck_Cost = 125
    Insurance = 40
    Under_Age=15
    Legal_Age=16
    Number_Of_Accidents=3
    #String Names
    First_Name=""
    Last_Name=""
    SUV=Truck=Compact_SUV=Economy=Type_Of_Car=0
    
    
    
    
    
    #Display Introduction
    print("<->"*32)

    print("""


  _____               _   _                            _          _____            _        _ 
 |  __ \             | | (_)                /\        | |        |  __ \          | |      | |
 | |__) | __ ___  ___| |_ _  __ _  ___     /  \  _   _| |_ ___   | |__) |___ _ __ | |_ __ _| |
 |  ___/ '__/ _ \/ __| __| |/ _` |/ _ \   / /\ \| | | | __/ _ \  |  _  // _ \ '_ \| __/ _` | |
 | |   | | |  __/\__ \ |_| | (_| |  __/  / ____ \ |_| | || (_) | | | \ \  __/ | | | || (_| | |
 |_|   |_|  \___||___/\__|_|\__, |\___| /_/    \_\__,_|\__\___/  |_|  \_\___|_| |_|\__\__,_|_|
                             __/ |                                                            
                            |___/

    \n\n""")    
    print("<->"*32)

    print("\nFirst name:")
    input(First_Name)
    print("\nLast name:")
    input(Last_Name)

    
    Legal_Age==int(input("\nEnter the age of the driver: "))
    if Under_Age<=Legal_Age:
        print("\nUser is underaged to rent a vehicle.")
    else:("\nYou may continue.")
    
    Number_Of_Accidents == int(input("\nPlease enter total amount of accidents: "))
    print("-"*50)
    if Number_Of_Accidents == 0:
        print("\nSelect one of the following categories from our garage.")
    elif Number_Of_Accidents == 1:
        print("\nSelect one of the following categories from our garage.")
    elif Number_Of_Accidents == 2:
        print("\nSelect one of the following categories from our garage.")
    elif Number_Of_Accidents == 3:
        print("\nThis user does not qualify to rent a car.")
    else:
        ("\nThis user does not qualify to rent a car")

    Type_Of_Car==(input("\nEconomy(A) Compact SUV(B) SUV(C) Truck(D)"))
    if Type_Of_Car==A:
        

   
        

   
    
    

   
            
    
   
   
    



main()
