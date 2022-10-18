from os.path import exists
from time import sleep
import os,time,random

def main():
    DartsIntro()

    MainMenu()

#return type: none
#parameters: none
#purpose: this function prompts the user for a selection of menu 
def MainMenu():
    
    print(f"\n{'*'*9}")
    print("Main Menu")
    print(f"{'*'*9}")
    print("\n1. Rules")
    print("2. Play Against Computer")
    print("3. Play Two Player Game")
    print("4. Stats Page")
    print("5. See credits")
    print("6. Quit")

    while True:
        try:
            select = 0
            selection=int(input("\nPlease select a menu option: "))
            if selection==1:
                BlindDartsGameRules()
                MainMenu()
                break
            elif selection==2:
                SinglePlayer()
                MainMenu()
                break
            elif selection==3:
                TwoPlayer()
                MainMenu()
                break
            elif selection==4:
                while select == 0:
                    select = input("1. Single Player Stats\n2. Two Player Stats\nInput a selection: ")
                    if select == "1":
                        print(ReadStats())
                    elif select == "2":
                        print(ReadStats2())
                    else:
                        print("\nInvalid selection. Please enter an option labeled 1-2\n")
                        sleep(1)
                        select = 0
                sleep(2)
                MainMenu()
                break
            elif selection==5:
                GameCredits()
                MainMenu()
                break
            elif selection==6:
                EndGame()
                break
            else:
                print("Invalid selection. Please enter an option labeled 1-6")
                MainMenu()
        except ValueError:
            print("Invalid Selection. Please enter an option labeled 1-6")
            MainMenu()
    exit

    

#return type: 1 string for highscore  
#parameters: none
#purpose: to read highscore
def ReadStats():
    f1 = open('highscoreSingleMode.txt','r')
    stats = f1.read()
    f1.close()
    return stats

def ReadStats2():
    f1 = open('highscoreTwoMode.txt','r')
    stats = f1.read()
    f1.close()
    return stats
#return type: none
#parameters: none
#purpose: display title
def DartsIntro():
    with open('BlindDartsIntro.txt') as f:
        contents = f.read()
        print(contents)

#return type: none
#parameters: none
#purpose: display rules
def BlindDartsGameRules():
    print("Blind Darts Game Rules:")
    print("-"*25)
    lines = []
    with open('DartsRules.txt') as f:
            lines = f.readlines()

    count = 0
    for line in lines:
        count += 1
        print(f'\nRule {count}: {line}')

#return type: none
#parameters: none
#purpose: display board
def DartBoard(User1,User2):
            score1=score2=100
            print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
            print("M I S S".center(20))
            print("----------------".center(20))
            print("|10|10|10|10|10|".center(20))
            print("----------------".center(20))
            print("|10|20|20|20|10|".center(20))
            print("----------------".center(20))
            print("|10|20|50|20|10|".center(20))
            print("----------------".center(20))
            print("|10|20|20|20|10|".center(20))
            print("----------------".center(20))
            print("|10|10|10|10|10|".center(20))
            print("----------------".center(20))
            print("M I S S".center(20))

#return type: result
#parameters: none
#purpose: pick a random number from the selection and return to user as result
def RandomScoreSelection():
    points = ['0','0','10','10','10','10','10','10','10','10','10','10','10','10','10','10','10','20','20','20','20','20','20','20','20','50']
    result = random.choice(points)
    return result

#Gameplay Animation
import os,time
os.system('cls') #Clear the screen
filenames = ["BlindDarts1.txt","BlindDartsTWO.txt","BlindDartsTHREE.txt",
             "BlindDartsFOUR.txt","BlindDartsFIVE.txt","BlindDartsSEVEN.txt"]

#return type: none
#parameters: none
#purpose: displays dart animation
def BlindDartsAnimator(filenames,delay = 0.1, repeat = 1): #Default setting for proper speed of animation
    frames = []
    for name in filenames:
        with open(name,"r",encoding="utf8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system('cls')

#return type: none
#parameters: none
#purpose: display credits
def GameCredits():
    print("Blind Darts Game Developers: ")
    print("-"*25)
    with open('GameCredits.txt') as f:
        contents = f.read()
        print(contents)

        
#return type: none
#parameters: none
#purpose: display end of game
def QUIT():
    with open('QUIT.txt') as f:
        contents = f.read()
        print(contents)
        
#return type: None
#parameters: Quit function
#purpose: display end of game
def EndGame():
    QUIT()
    print("\nBullseye! Thank you for playing!")
    exit

#return type: 
#parameters: DartBoard Function, Random Number Selection Function, Read and Logging High Score Functions
#purpose: play against the computer
def SinglePlayer():
    player = 0
    score1 = score2 = 100
    HitCount=MissCount=GoodCount=BullsCount=0
    print(f"\n{'*'*35}")
    User1 = input("Player 1, please enter your name: ").strip()
    User1 = User1.capitalize()
    if User1 == "":
        User1 = "Player 1"
    User2 = "CPU"
    print(f"{User1}, welcome to Blind Darts!\n")
    DartBoard(User1,User2) #Board Display to show player their odds
    print("\nYour eyes are gone but you sense the board. Throw your darts until you can no more!!\n")
    sleep(1)
    
    while score1 <= 200 and score1 > 0 and score2 <= 200 and score2 > 0:
        dart = 3
        while player == 0 and score1 > 0 and score2 > 0: #Player 1's turn
            if dart > 0:
                print(f"{User1}'s turn!!")
                sleep(.5)
                print("Score:",score1)
                sleep(.5)
                print(f"Darts: {dart}\n")
                sleep(.5)
                input(f"Cast your dart? (Hit 'ENTER'): ")
                BlindDartsAnimator(filenames,delay = 0.1, repeat = 1)
                deduct = RandomScoreSelection()
                if deduct == '0':
                    dart -= 1
                    score1 -= 0
                    MissCount +=1
                    print('MISS\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                   
                elif deduct == '10':
                    dart -= 1
                    score1 -= 10
                    HitCount +=1
                    print('HIT\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                    
                elif deduct == '20':
                    dart -= 1
                    score1 -= 20
                    GoodCount  +=1
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                    
                elif deduct == '50':
                    dart -= 1
                    score1-=50
                    BullsCount = +1
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                    
            elif dart == 0:
                print("TURN CHANGE\n")
                print(f"{'-'*20}")
                player = 1
                dart = 3
        while player == 1 and score1 > 0 and score2 > 0: #CPU Turn
            while dart > 0:
                print("CPU Turn")
                sleep(.5)
                print("Score:",score2)
                sleep(.5)
                print(f"Darts: {dart}\n")
                sleep(1)
                print("The CPU is thinking...")
                sleep(.5)
                print(".")
                sleep(.5)
                print(".")
                time.sleep(.5)
                print("THE DART LAUNCHES!")
                sleep(.1)
                BlindDartsAnimator(filenames,delay = 0.1, repeat = 1)
                deduct = RandomScoreSelection()
                if deduct == '0':
                    dart -= 1
                    score2 -= 0
                    print('MISS\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '10':
                    dart -= 1
                    score2 -= 10
                    print('HIT\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '20':
                    dart -= 1
                    score2 -= 20
                    print('GOOD HIT\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '50':
                    dart -= 1
                    score2 -=50
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
            print("TURN CHANGE\n")
            print(f"{'-'*20}")
            player = 0
            dart =3
        if score1 <= 0:
            print(f"Congrats Player 1, your score has reached {score1}. YOU WIN!")
            
        elif score2 <= 0:
            print(f"The CPU has reached a score of {score2}. YOU LOSE!")
            
        f = open('highscoreSingleMode.txt', 'w')
        f.write(f"--Stats Reflected By Recent Game--\n\nMisses: {MissCount}\nHits: {HitCount}\nGoods: {GoodCount}\nBullseye's: {BullsCount}\n\n")
        f.close()

#return type: 
#parameters:  DartBoard Function, Random Number Selection Function, Read and Logging High Score Functions
#purpose: play two player game         
def TwoPlayer():
    player = 0
    HitCount1=MissCount1=GoodCount1=BullsCount1=0
    HitCount2=MissCount2=GoodCount2=BullsCount2=0
    score1 = score2 = 100
    User1 = User2 = ""
    
    print(f"\n{'*'*35}")
    User1 = input("Player 1, please enter your name: ").strip()
    User2 = input("Player 2, please enter your name: ").strip()
    User1 = User1.capitalize()
    User2 = User2.capitalize()
    if User1 == "":
        User1 = "Player 1"
    if User2 == "":
        User2 = "Player 2"

    print(f"{User1} and {User2}, welcome to Blind Darts!\n")
    DartBoard(User1,User2) #Board Display to show player their odds
    
    print("\nYour eyes are gone but you sense the board. Throw your darts until you can no more!!\n")
    sleep(1)
    
    while score1 <= 200 and score1 > 0 and score2 <= 200 and score2 > 0:
        dart = 3
        while player == 0 and score1 > 0 and score2 > 0: #Player 1's turn
            if dart > 0:
                print(f"{User1}'s turn!!")
                sleep(.5)
                print("Score:",score1)
                sleep(.5)
                print(f"Darts: {dart}\n")
                sleep(.5)
                input(f"Hit 'ENTER' to cast your dart : ")
                BlindDartsAnimator(filenames,delay = 0.1, repeat = 1)
                deduct = RandomScoreSelection()
                if deduct == '0':
                    dart -= 1
                    score1 -= 0
                    MissCount1 += 1
                    print('MISS\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
                elif deduct == '10':
                    dart -= 1
                    score1 -= 10
                    HitCount1 += 1
                    print('HIT\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
                elif deduct == '20':
                    dart -= 1
                    score1 -= 20
                    GoodCount1 += 1
                    print('GOOD HIT\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
                elif deduct == '50':
                    dart -= 1
                    score1-=50
                    BullsCount1 += 1
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
            elif dart == 0:
                print("TURN CHANGE\n")
                print(f"{'-'*20}")
                player = 1
                dart = 3
        while player == 1 and score1 > 0 and score2 > 0: #Player 2 Turn
            if dart > 0:
                print(f"Now it's {User2}'s turn!!")
                sleep(.5)
                print("Score:",score2)
                sleep(.5)
                print(f"Darts: {dart}\n")
                sleep(.5)
                input(f"Hit 'ENTER' to cast your dart : ")
                BlindDartsAnimator(filenames,delay = 0.1, repeat = 1)
                deduct = RandomScoreSelection()
                if deduct == '0':
                    dart -= 1
                    score2 -= 0
                    MissCount2 += 1
                    print('MISS\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
                elif deduct == '10':
                    dart -= 1
                    score2 -= 10
                    HitCount2 += 1
                    print('HIT\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
                elif deduct == '20':
                    dart -= 1
                    score2 -= 20
                    GoodCount2 += 1
                    print('GOOD HIT\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n")  
                elif deduct == '50':
                    dart -= 1
                    score2-=50
                    BullsCount2 += 1
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[{User1} - {score1}]{'-'*5}[{User2} - {score2}]{'-'*5}\n\n") 
            elif dart == 0:
                print("TURN CHANGE\n")
                print(f"{'-'*20}")
                player = 0
                dart = 3
        if score1 <= 0:
            print(f"Congrats {User1}, your score has reached {score1}. YOU WIN!")
            
        elif score2 <=0:
            print(f"Congrats {User2}, your score has reached {score2}. YOU WIN!")
            
        f = open('highscoreTwoMode.txt', 'w')
        f.write(f"--Stats Reflected By Recent Game--\n\n{User1} Stats\n\nMisses: {MissCount1}\nHits: {HitCount1}\nGoods: {GoodCount1}\nBullseye's: {BullsCount1}\n\n{User2} Stats\n\nMisses: {MissCount2}\nHits: {HitCount2}\nGoods: {GoodCount2}\nBullseye's: {BullsCount2}\n\n")
        f.close()
            
                
main()
