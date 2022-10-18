def getGuess(first, last):
    while 1:  # this while loop iterates to validate user input
        print("Enter your guess (", first, "-", last, "): ", end="")
        guess = int(input())  # takes input of user guess
        if first <= guess <= last:  # checks if guess lies in range first to last
            break # control jumps out of for loop
        else:  # this else will again make control execute while loop
            print("Error ... Incorrect number. Try again")
            continue

    return guess


def guessWin(number, guess):

    # checks if random number is less than user number
    if number < guess:
        print(" --->  ", guess, "is too High ...\n")
        return False

    # if random number is greater than user number
    elif number > guess:
        print(" --->  ", guess, "is too Low ...\n")
        return False

    # if user number equal with random number
    elif guess == number:
        print("\nCongratulations ... You guessed the Mistery Number!")
        return True


if __name__ == '__main__':

    print("Guess the Mystery number ... \n")
    roundGame = 1
    choice = 'y'
    first = 1
    last = 100
    while choice != 'n':  # this while loop iterates until n is not entered to stop the game
        randomNumber = random.randint(first, last)  # gets the random number in the range 1 to 100
        for roundGame in range(7):  # this for loop iterates 7 times i.e. 7 rounds
            print("Round", roundGame + 1, "of 7")
            print("---------------------------------")

            guess = getGuess(first, last)  # calls function getGuess to take user input of guess

            result = guessWin(randomNumber, guess)  # calls function guessWin to compare guess with random number

            if result == True:  # checks if value returned by function is true then
                break  # control jumps out of for loop

        print("\nWould you like to try again (y/n)? ", end="")  # ask user if want to continue or not
        choice = input()  # take input of choice
