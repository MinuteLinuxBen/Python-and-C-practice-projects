from os.path import exists
from time import sleep
import os,time,random
def MainMenu():
    DartsIntro()
    print("\n1. See Rules")
    print("2. VS CPU")
    print("3. 2 Player Game")
    print("4. Leaderboard")
    print("5. See credits")
    print("6. Quit")

    while True:
        try:
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
                # Append file for high score
                # from player's name
                ReadHighScore()
                MainMenu()
                break
            elif selection==5:
                GameCredits()
                MainMenu()
                break
            elif selection==6:
                EndGame()
                ReadHighScore()
                break
            else:
                print("Invalid selection. Please enter an option labeled 1-4")
                MainMenu()
        except ValueError:
            print("Invalid Selection. Please enter an option labeled 1-4")
    exit

def LogHighScore(highScore = 0):
    # ensure python file will be closed using `with` statement
    with open('highscore.txt', 'w') as f:
        f.write(str(highScore))
        
def ReadHighScore():
    # obtain high score from txt file
    f = open("highscore.txt", "r")
    txt = f.read()
    print(f"The current score is: {txt}")
    f.close()
    return txt

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
def DartBoard():
            score1=score2=150
            print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
            print("M I S S".center(20))
            print("----------------".center(20))
            print("10|10|10|10|10|".center(20))
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
def GameCredits():
    print("Blind Darts Game Developers: ")
    print("-"*25)
    with open('GameCredits.txt') as f:
        contents = f.read()
        print(contents)
        
def QUIT():
    with open('QUIT.txt') as f:
        contents = f.read()
        print(contents)

def EndGame():
    QUIT()
    print("\nBullseye! Thank you for playing!")
    exit

#VS CPU Mode
def SinglePlayer():
    player = 0
    score1 = score2 = 150
    DartBoard() #Board Display to show player their odds
    print("\nYour eyes are gone but you sense the board. Throw your darts until you can no more!!\n")
    sleep(1)
    
    while score1 <= 200 and score1 > 0 and score2 <= 200 and score2 > 0:
        dart = 3
        while player == 0 and score1 > 0 and score2 > 0: #Player 1's turn
            if dart > 0:
                print("Player 1's turn!!")
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
                    print('MISS\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '10':
                    dart -= 1
                    score1 -= 10
                    print('HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '20':
                    dart -= 1
                    score1 -= 20
                    print('GOOD HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '50':
                    dart -= 1
                    score1-=50
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
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
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '10':
                    dart -= 1
                    score2 -= 10
                    print('HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '20':
                    dart -= 1
                    score2 -= 20
                    print('GOOD HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
                elif deduct == '50':
                    dart -= 1
                    score2 -=50
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[CPU - {score2}]{'-'*5}\n\n") 
            print("TURN CHANGE\n")
            print(f"{'-'*20}")
            player = 0
            dart =3
        if score1 <= 0:
            print(f"Congrats Player 1, your score has reached {score1}. YOU WIN!")
        elif score2 <= 0:
            print(f"The CPU has reached a score of {score2}. YOU LOSE!")
#2 Player Mode
def TwoPlayer():
    player = 0
    score1 = score2 = 150
    DartBoard() #Board Display to show player their odds
    print("\nYour eyes are gone but you sense the board. Throw your darts until you can no more!!\n")
    sleep(1)
    
    while score1 <= 200 and score1 > 0 and score2 <= 200 and score2 > 0:
        dart = 3
        while player == 0 and score1 > 0 and score2 > 0: #Player 1's turn
            if dart > 0:
                print("Player 1's turn!!")
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
                    print('MISS\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
                elif deduct == '10':
                    dart -= 1
                    score1 -= 10
                    print('HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
                elif deduct == '20':
                    dart -= 1
                    score1 -= 20
                    print('GOOD HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
                elif deduct == '50':
                    dart -= 1
                    score1-=50
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
            elif dart == 0:
                print("TURN CHANGE\n")
                print(f"{'-'*20}")
                player = 1
                dart = 3
        while player == 1 and score1 > 0 and score2 > 0: #Player 2 Turn
            if dart > 0:
                print("Player 2's turn!!")
                sleep(.5)
                print("Score:",score2)
                sleep(.5)
                print(f"Darts: {dart}\n")
                sleep(.5)
                input(f"Cast your dart? (Hit 'ENTER'): ")
                BlindDartsAnimator(filenames,delay = 0.1, repeat = 1)
                deduct = RandomScoreSelection()
                if deduct == '0':
                    dart -= 1
                    score2 -= 0
                    print('MISS\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
                elif deduct == '10':
                    dart -= 1
                    score2 -= 10
                    print('HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
                elif deduct == '20':
                    dart -= 1
                    score2 -= 20
                    print('GOOD HIT\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n")  
                elif deduct == '50':
                    dart -= 1
                    score2-=50
                    print('BULLSEYE\n')
                    print(f"{'-'*5}[Player 1 - {score1}]{'-'*5}[Player 2 - {score2}]{'-'*5}\n\n") 
            elif dart == 0:
                print("TURN CHANGE\n")
                print(f"{'-'*20}")
                player = 0
                dart = 3

        if score1 <= 0:
            print(f"Congrats Player 1, your score has reached {score1}. YOU WIN!")
            highScore = ReadHighScore()
            if int(highScore) < score1:
                print("New high score!! - " + str(score))
                LogHighScore(score1)
            else:
                print("High Score: " + str(highScore))
        elif score2 <=0:
            print(f"Congrats Player 2, your score has reached {score2}. YOU WIN!")
            highScore = ReadHighScore()
            if int(highScore) < score2:
                print("New high score!! - " + str(score))
                LogHighScore(score2)
            else:
                print("High Score: " + str(highScore))
MainMenu()
