def BlindDartsBoard():
    characterX = 1
    characterY = 1

    CharacterPosition = "| A |"

    board = [["|   |" for a in range(5)] for b in range(5)]

    board[characterX][characterY] = CharacterPosition

    while True:
        for i in board:
            print("----- ----- ----- ----- -----")
            print(" ".join(i))
            print("----- ----- ----- ----- -----")
            

            print("Controls:")
            print("Up: W")
            print("Down: S")
            print("Left: A")
            print("Right: D")

            direction = input("Please enter one of the following choices: ")
            if direction == "W":
                board[characterX][characterY] = "|   |"
                characterX -=1
                board[characterX][characterY] = "| A |"
            elif direction =="S":
                board[characterX][characterY] = "|   |"
                characterX +=1
                board[characterX][characterY] = "| A |"
            elif direction == "A":
                board[characterX][characterY] = "|   |"
                characterY -=1
                board[characterX][characterY] = "| A |"
            elif direction == "D":
                board[characterX][characterY] = "|   |"
                characterY +=1
                board[characterX][characterY] = "| A |"



BlindDartsBoard()
