from os.path import exists

#Main Function for the game.
def MainMenu():
    DartsIntro()
    print("\n1. See Rules")
    print("2. Play Against Computer")
    print("3. Play 2 Player Game")
    print("4. See High Score")
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
                # 1st Play game function
                DartsGameBoard()
                MainMenu()
                break
            elif selection==3:
                # 2nd Play game function
                # Two player game
                DartsGameBoard(True)
                MainMenu()
                break
            elif selection==4:
                # Append file for high score
                # from player's name
                # Highscore()
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
                print("Invalid selection. Please enter an option labeled 1-4")
                MainMenu()
        except ValueError:
            MainMenu()
           
    exit

#1 Game's title/Inroduction
def DartsIntro():
    with open('BlindDartsIntro.txt') as f:
        contents = f.read()
        print(contents)

#2 Game's Rules
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



#Gameplay animation
import os,time
os.system('cls') #Clear the screen
filenames = ["BlindDarts1.txt","BlindDartsTWO.txt","BlindDartsTHREE.txt",
             "BlindDartsFOUR.txt","BlindDartsFIVE.txt","BlindDartsSEVEN.txt"]

# Used after every player(s) turn
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


#3 Game Credits
def GameCredits():
    print("Blind Darts Game Developers: ")
    print("-"*25)
    with open('GameCredits.txt') as f:
        contents = f.read()
        print(contents)

#Quit Picture
def QUIT():
    with open('QUIT.txt') as f:
        contents = f.read()
        print(contents)


#4 Function to end Game
def EndGame():
    QUIT()
    print("\nBullseye! Thank you for playing!")
    exit


def LogHighScore(highScore = 0):
    # ensure python file will be closed using `with` statement
    with open('highscore.txt', 'w') as f:
        f.write(str(highScore))


def ReadHighScore():
    # obtain high score from txt file
    f = open("highscore.txt", "r")
    txt = f.read()
    f.close()
    return txt


from random import randint
def DartsGameBoard(isTwoPlayer = False):
    # Create a random function to position where the dart has to go to gain a point.
    characterX = 2
    characterY = 2

    characterPosition = "|  |"

    board = [["|  |" for a in range(5)] for b in range(5)]

    board[characterX][characterY] = characterPosition

    # generate random number
    num = randint(0, 24)
    row = int(num / 5)
    col = int(num % 5)

    # game scoring system
    score = 25

    # current player true = player 1
    # current player false = player 2
    currPlayer = True
    player = ""
    
   
    while True:
        for i in board:
            print("---- ---- ---- ---- ----")
            print(" ".join(i))
            print("---- ---- ---- ---- ----")
        print("Guess the correct position on the dart board!")
        print("\nTurn CAPS LOCK on")
        print("Controls:")
        print("Up: W")
        print("Down: S")
        print("Left: A")
        print("Right: D")

        if isTwoPlayer:
            player = f"Player 1 - " if currPlayer else f"Player 2 - "
            currPlayer = not currPlayer

        if score == 0:
            # enter game lose logic here
            print("game lost - too many guesses - score: " + str(score) + "pts")
            break

        direction = input(player + " please select the following moves: ")
        

        # every guess costs one point from the players score
        score -= 1

        # execute animation
        board[characterX][characterY] = "|  |"
        BlindDartsAnimator(filenames,delay = 0.1, repeat = 1)

        # player controls logic
        if direction == "W":
            characterX -= 1
        elif direction == "S":
            characterX += 1
        elif direction == "A":
            characterY -= 1
        elif direction == "D":
            characterY += 1

        if row == characterX and col == characterY:
            # enter win logic here
            print("\n\n\n\n\n")
            print(player + "game won - score: " + str(score) + "pts")

            if not exists("highscore.txt"):
                LogHighScore(score)
            else:
                highScore = ReadHighScore()
                if int(highScore) < score:
                    print("New high score!! - " + str(score))
                    LogHighScore(score)
                else:
                    print("High Score: " + str(highScore))

            print("\n\n\n\n\n")
            break

        board[characterX][characterY] = "| o|"


MainMenu()
