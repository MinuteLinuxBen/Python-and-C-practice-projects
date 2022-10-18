# Benjamin Smith
# Jan 26, 2022
# The purpose of this program is to calculate the total cost of a bill at a given restaurant/establishment.
# This billing calculator takes into account the cost of beverages, food, sales tax, and tipping services.
# Define the main function.
# Define and intialize variables.
# The bill is reflected in a integer or float for beverages, food, tipping, and sales tax.
# Display intro
# The style of ascii word art "Casino Royal Billing Service"".
# prompt customer the cost of beverages.
# prompt customer the cost of food.
# prompt customer the cost of tipping. The suggested amount is 20%.
# Calculate sales tax from the total cost of food (food * 7% sales tax).
# Calculate sales tax from the total cost of (beverages * 7% sales tax).
# Calculate the grand total of the bill ( sales taxed food + sales taxed beverages).  
# Calculate a suggested tipping amount that includes 15, 18, and 20%.
# Calculate tip using grand total + 20% Tip percentage.
# Display the cost of food + sales tax 7%.
# Display the cost of beverages + sales tax 7%.
# Display grand total of food and beverages with apporiate tax amount.
# Display tipping amount 20% is recommended. If no, then display a different screen for values 15-20%.
# Display the apporiate amounts that match the grand total and reflected tipping amounts selected.
# Display Outro.
# Play sound() "windows beep" after bill is paid in full.
# Display "Thank you for using "Casino Royal Billing Service"".

# Call main function 

import winsound
def main():
  


    # Dispaly introduction
    print("$"*105)
   
    print("""
    
      
 _______  _______  _______ _________ _        _______    _______  _______           _______  _         
(  ____ \(  ___  )(  ____ \\__   __/( (    /|(  ___  )  (  ____ )(  ___  )|\     /|(  ___  )( \        
| (    \/| (   ) || (    \/   ) (   |  \  ( || (   ) |  | (    )|| (   ) |( \   / )| (   ) || (        
| |      | (___) || (_____    | |   |   \ | || |   | |  | (____)|| |   | | \ (_) / | (___) || |        
| |      |  ___  |(_____  )   | |   | (\ \) || |   | |  |     __)| |   | |  \   /  |  ___  || |        
| |      | (   ) |      ) |   | |   | | \   || |   | |  | (\ (   | |   | |   ) (   | (   ) || |        
| (____/\| )   ( |/\____) |___) (___| )  \  || (___) |  | ) \ \__| (___) |   | |   | )   ( || (____/\  
(_______/|/     \|\_______)\_______/|/    )_)(_______)  |/   \__/(_______)   \_/   |/     \|(_______/  
                                                                                                       
 ______  _________ _        _       _________ _        _______                                         
(  ___ \ \__   __/( \      ( \      \__   __/( (    /|(  ____ \                                        
| (   ) )   ) (   | (      | (         ) (   |  \  ( || (    \/                                        
| (__/ /    | |   | |      | |         | |   |   \ | || |                                              
|  __ (     | |   | |      | |         | |   | (\ \) || | ____                                         
| (  \ \    | |   | |      | |         | |   | | \   || | \_  )                                        
| )___) )___) (___| (____/\| (____/\___) (___| )  \  || (___) |                                        
|/ \___/ \_______/(_______/(_______/\_______/|/    )_)(_______)                                        
                                                                                                       
                          
                                                            
    \n\n""")
    print(f"{'$'*105}\n\n")


    print("-"*40)
    print("\n\n Please select from our menu!")
    print("-"*40)
    print("\nfood")
    print("-"*40)
    print('\n Chicken Pad Thai: $10.00')
    print('\n Tom Kha gai soup: $5.00')
    print('\n Coconut curry: $8.00')
    print("-"*40)
    print("\n\n Beverages:")
    print(f"{'-'*40}\n\n")
    print('\n Beer: $3.00')
    print('\n Soda: $2.00')
    print('\n Water: $1.00')
    print("-"*40)
    cost_for_food = float(input('\nEnter charge for food: $'))
    print(f"{'-'*40}\n\n")
    print("-"*40)
    cost_for_beverages = float(input('\nEnter charge for beverages: $'))
    print(f"{'-'*40}\n\n")

    # Delcare all variables
    tipping_percent = .20
    other_tipping_amounts = .18
    other_tipping_percent = .15
    sales_tax = .07
    #Define the arithmetic by correlating the needed variables for the calculator
    tipping_percent = (cost_for_food * tipping_percent + cost_for_beverages * tipping_percent)
    other_tipping_percent = (cost_for_food * other_tipping_percent + cost_for_beverages * other_tipping_percent)
    other_tipping_amounts = (cost_for_food * other_tipping_amounts + cost_for_beverages * other_tipping_amounts) 
    sales_tax = (cost_for_food * sales_tax + cost_for_beverages*sales_tax)
    grand_total = cost_for_food + cost_for_beverages + tipping_percent + sales_tax

    # Execute all defined variables.
    # Use the information to print each function
    print('\ncost of food = $', format(cost_for_food, ',.2f'), sep='')
    print('\nCost of beverages = $', format(cost_for_beverages, ',.2f'), sep='')
    print("-"*40)
    print('\nCost Reflected before sales tax and tipping services = $', format(cost_for_food + cost_for_beverages, '.2f'), sep='')
    print("-"*40)
    print('\nTip @ 20% = $', format(tipping_percent, ',.2f'), sep='')
    print('\nTip @ 18% = $', format(other_tipping_amounts, ',.2f'), sep='')
    print('\nTip @ 15% = $', format(other_tipping_percent, ',.2f'), sep='')
    print("-"*40)
    print('Sales tax = $', format(sales_tax, ',.2f'), sep='')
    print('Grand total with recommended 20% tip = $', format(grand_total, ',.2f'), sep='', end='\n\n')
    print("-"*40)
    # Outro
    #import winsound
    import winsound
    # play the sound
    #stop window from closing
    winsound.PlaySound("sound2", winsound.SND_ASYNC)
    delay = input(" Press ENTER when done.")

    #THANK YOU and hope you enjoyed my first independent python project for calculating costs at a restaurant/establishment
    # Call main function
    
main()
        

