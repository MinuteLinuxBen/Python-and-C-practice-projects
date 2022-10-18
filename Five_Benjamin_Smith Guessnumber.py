#Benjamin Smith
#3/22/2022
#GuessNumber.py
#The purpose of this program is allow the user to guess
#the range of 1-100 is used
#Within 1-100 the user only gets a hint that he/she
#has a guess "Too High" or "Too Low".
#The user can get the guess right and the program
#will also congratulate their correct guess.


#import the random number library 
import random
#import the turtle graphics library for drawing a star/sun shape for declared winner
from turtle import *
#Define the first function so the random number library has the ability to generate
# a number different or the same as the user's guess.
def getGuess(first_rando, last_rando):
    while 1==1:  # this while loop iterates automatically so the user is validated
        print("Please enter a number guess (", first_rando, "~", last_rando, "): ", end="")
# take the given number from the user
        guess = int(input())  
        if first_rando <= guess <= last_rando:  # Compares the range of numbers with the user's guess
            break # control jumps out of for loop
        else:  #force close the while loop
            print("Error ... Number must be a positive or whole number. Try again")
            continue

    return guess


#define the GuessWin function so the user can have a way
#to see if their answer/number is correct. 
def GuessWin(bot_num, guess_to_win):
#Import time to set a dramatic effect for the results
    import time
    
    # checks if random number is less than user number
    if bot_num < guess_to_win:
        print("\t\t(ಥ﹏ಥ)")
        time.sleep(2)
        print(" >->->  ", guess_to_win, "is too High! ...\n")
        return False

    # if random number is greater than user number
    elif bot_num > guess_to_win:
        print("\t\t(ಠ ಠ)")
        print("\t\t  0   ")
        time.sleep(2)
        print(" ->->->  ", guess_to_win, "is Too Low! ...\n")
        return False

    # if user number equal with random number
    elif guess_to_win == bot_num:
        print("\nCongratulations ... With a 7% chance you managed to guess right!")
        print("Here is a bright star for your troubles!...")
       
        color('red', 'orange')
        begin_fill()
        while True:
            forward(200)
            left(170)
            if abs(pos()) < 1:
                break
        print("WINNER!")
        
        return True


#Return : 3 strings for "Too High, Too Low, and Congratulations!"
#Parameters: for range of 1-7 giving the user only 7 tries to guess
#This function will return the result of the number guessed.
def main(): 

    print("Guess the Lucky Mystery number ... \n")
    roundGame= 1
    pick = 'y'.capitalize
    first_rando = 1
    last_rando = 100

    import time
    while pick != 'n':  # this acts as a quit to stop the loop of proceeding to play a new game
        #Scopes in (1-100) as a list of numbers to go through
        random_value = random.randint(first_rando, last_rando)  
        for roundGame in range(7):  # this for loop iterates 7 times i.e. 7 rounds
            print("Ding!")
            time.sleep(1)
            print("Ding!")
            print("(ง°ل͜°)ง")

            print("Round", roundGame+ 1, "of 7")
            print("Guess!")
            print("-"*30)

            guess = getGuess(first_rando, last_rando)  

            result = GuessWin(random_value, guess)  

            if result == True:  # The results have to be compared to true so the player
                #can keep playing the same game over and over again.
                break  #No Else or Elif need because the Boolean option loops the program from the
            #beginning

        print("\nWould you like to try again [y/n]? ", end="")  # ask user if want to con
        choice = input()  # Input of the choice is Y/N
main()
