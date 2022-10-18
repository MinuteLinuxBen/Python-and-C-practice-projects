#Ketnie Domond

from time import sleep
import random

def main():
    DartsIntro()

    MainMenu()

#return type: 1 string for selection from menu
#parameters: none
#purpose: this function prompts the user for a selection of menu 
def MainMenu():
    
    selection = 0

    print(f"\n{'*'*9}")
    print("Main Menu")
    print(f"{'*'*9}")
    print("1) Rules \n2) Play Against Computer \n3) Play 2 Player Game \n4) See Score \n5) Quit ")

    while selection < 1 or selection > 6:
        #try:
                selection = float(input("Please enter an option from the list above: "))
                if selection < 1 or selection > 6:
                        print("Invalid, your selection must be between 1-5.")

                elif selection == 1: 
                        BlindDartsGameRules()
                        MainMenu()
                elif selection == 2:
                        return "2"
                elif selection == 3:
                        TwoPlayer()
                elif selection == 4:
                        ScoreDisplay()
                        sleep(3)
                        MainMenu()
                elif selection == 5:
                        EndGame()
                else:
                        print("...")
        #except:
        #       print("Please enter a number between 1-5.")
        

#return type: none
#parameters: none
#purpose: display title
def DartsIntro():
    with open('BlindDartsIntro.txt') as f:
        contents = f.read()
        print(contents)

#return type: none
#parameters: none
#purpose: diplay rules
def BlindDartsGameRules():
    print("- The dart board is a 5x5 square board.")
    sleep(.5)
    print("- Points are on each spaces, starting with 10 at the edge,"
          "then 20 in the inner layer and 50 in the center")
    print("- Each player starts with 200 points.")
    print("- Points get deducted based on which space a dart hits on the board.")
    print("- Hit a 10 ... -10 \nHit a 20 ... -20 \n Hit 50 ... -50")
    print("There is also a possibility to miss ... -0")
    print("- 2 darts can be thrown per turn by each player.")
    print("- Turns keep going until one of the players reach 0 points.")
    print("- Where the dart land will be based on a random number generator.")

#return type: none
#parameters: none
#purpose: randomize the dart value        
def launchdart():
    dart = random.randint(0, 10, 20, 50)
    score = 200
    if dart == 0:
        print("MISS")
        #score -= 0
    elif dart == 10:
        print("HIT")
        #score -= 10    
    elif dart == 20:
        print("GREAT HIT!")
        #score -= 20
    elif dart == 50:
        print("BULLSEYE!!!")
        #score -= 50
    

    return dart

def ScoreDisplay():
    score1 = 200
    score2 = 200

    print(f"Player 1 - Current Score: {score1}")
    sleep(.5)
    print(f"Player 2 - Current Score: {score2}")
    
    #if result == "10":
     #   score -= 10
    #elif result == "20":
     #   score -= 20
    #elif result == "50":
     #   score -=50
    #elif result == "0":
     #   score -= 0
        
    return score1
    return score2

#def WinLose(score):    


def TwoPlayer():
    rounds = 10
    turn = 2
    User1 = User2 = ""

    print(f"\n{'*'*35}")
    User1 = input("Player 1, please enter your name: ").capitalize()
    User2 = input("Player 2, please enter your name: ").capitalize()

    print(f"{User1} and {User2} Welcome to Blind Darts\n")
    
    print(f"Turn 1 - {User1}")
    print("Dart is being launched...")
    sleep(1)
    
    launchdart()

#return type: none
#parameters: none
#purpose: display end of game        
def EndGame():
    
    print(f"\n{'*'*33}")
    print("BULLSEYE!!! THANK YOU FOR PLAYING!")

    sleep(1)
    
    with open('QUIT.txt') as f:
        contents = f.read()
        print(contents)
        
           
main()
    



