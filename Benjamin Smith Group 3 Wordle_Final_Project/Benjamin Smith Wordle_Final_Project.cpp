/*
    Authors:  Benjamin Smith, Domenica Jaramillo, Saul Abreu
    Wordle.cpp
    4/20/2022

   Purpose:
            This game was created as a clone to wordle. This game was purchased by The New York Times.
            Spelling a 5-letter word is not a challenge compared to guessing at random spots in
            a matrix square. The user must get a word correct and placement markers 
            are used as clues until the user guesses correctly within the given amount of tries of the game.
            The original version includes a time function of some kind. This game only includes a looped version 
            based on the user's choice to keep playing.
   
   Input: Prompt user for options
           1.See Rules
           2.Play Game
           3.Quit
    Processing
        1. The words are extracted from a txt file
        2. The words equal to 100 and the srand function randomly picks a word
            from the pool of words
        3. A 2d array is stored within another 2d array. This allows for each letter
            to be printed seperately in each seperate box. 
        4. The user has up to six tries including the first empty column to guess the word
            correctly.
        5. Colours are used to dictate if the placement is correct. This acts as a clue for the user.
        6. The game loops again until the user decides to quit.

    Output: 
        1. The user sees the rules, game, or is closed out of the program
            depending on the case statements (1-3). 
        2. The same board is used until it is filled with all possible attempts
        3. Colour code is an indicator, and series of all green letters and a friendly message
           indicates if the user gets the game correct.
*/

//Header Files
#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#include<cstdlib>
#include<time.h>
using namespace std;

#define len 5
#define wid 6

//the following are UBUNTU/LINUX console colours. 
//Side note: Our team had issues with the windows example provided.
//            We did research and found this worked as an alternative

#define RESET   "\033[0m"        // Reset  //
#define GREEN   "\033[32m"      // Green  //
#define YELLOW  "\033[33m"     // Yellow //
#define GRAY    "\033[1;30m"  // Gray   //


//Function Prototypes
void GameRules();
string ChooseWord();
void PlayGame();
void UpdateWordleGrid(char** grid, int** colorGrid, string text, string answer, int currRow);
void PrintWordleGrid(char** grid, int** colorGrid);
char** CreateWordleGrid();
int** CreateWordleColorGrid();
bool IsValidWordle(string guess);
int ProcessChar(string answer, char currChar, int currIndex);


/*
parameter: currChar The current character in the guess being processed
parameter: answer Word pulled from txt file of possible answers
parameter: currIndex Index of character made in guess

Positions of the coloring in order to stay within the build of the square
1: Character is in the correct location in the string
0: Character exists elsewhere in the string
-1: Character does not exist in string
*/
int ProcessChar(string answer, char currChar, int currIndex) {
    if (answer.at(currIndex) == currChar) {
        return 1;
    }
    else if (answer.find(currChar) < answer.length()) {
        return 0;
    }

    return -1;
}


/*
parameter: The grid is updated with a correct guess in this function
*/
void UpdateWordleGrid(char** grid, int** colorGrid, string text, string answer, int currRow)
{
    for (int i = 0; i < len; i++) {
        colorGrid[currRow][i] = ProcessChar(answer, text.at(i), i);
        grid[currRow][i] = text.at(i);
    }
}


/*
parameter: guess Users input when guessing wordle
Ensure length is valid wordle guess
*/
bool IsValidWordle(string guess) {
    return guess.length() == 5;
}



/*
Creates 2-dimensional array from the provided defintions of the dimensions.
*/
char** CreateWordleGrid() {

    
    char** grid;
    grid = new char* [len];

    for (int i = 0; i < len; i++) {
        grid[i] = new char[wid];

        for (int j = 0; j < wid; j++) {
            grid[i][j] = ' ';
        }
    }

    return grid;
}

/*
Creates 2-dimensional array from provided dimension definitions

*/
int** CreateWordleColorGrid() {

    // some ugly pointer logic
    int** grid;
    grid = new int* [len];

    for (int i = 0; i < len; i++) {
        grid[i] = new int[wid];

        for (int j = 0; j < wid; j++) {
            // -2 equates to characters that have not been processed yet
            grid[i][j] = -2;
        }
    }

    return grid;
}

/*
Print grid
This provides the needed action to colour each letter depending on correctness
*/
void PrintWordleGrid(char** grid, int** colorGrid) {
  for (int i = 0; i < len; i++) {
    cout <<" "<<"---------------------"<<endl;
    for (int j = 0; j < wid; j++) {
      if (colorGrid[i][j] == 0) {
        cout << " | " << YELLOW << grid[i][j] << RESET;
      } else if (colorGrid[i][j] == 1) {
        cout << " | "<< GREEN << grid[i][j] << RESET;
      } else {
        // no color
        cout << " | " << grid[i][j];
      }
    }

    cout << endl;
  }
  cout <<" "<<"---------------------"<<endl;
}

/*
Print game rules
Create a .txt file and read in and create a case statement for the user to read from this.
*/
void GameRules()
{
    fstream myFile;
    myFile.open("rules.txt", ios::in);
    if (myFile.is_open()) {
        string line;
        cout << endl;
        while (getline(myFile, line)) {
            cout << line << endl;
        }
        myFile.close();
        cout << endl;
    }
}


/*
Pull in all 100 words from OneHundredWords.txt
*/
string ChooseWord()
{
    //rand() will produce the same value every time without a time seed
    //Included this if the time-function was to be used
    
    srand(time(NULL));

    int wordIndex = rand() % 100;
    int currIndex = 0;
    string word;

    fstream myFile;
    myFile.open("OneHundredWords.txt", ios::in);
    if (myFile.is_open()) {
        string line;
        while (getline(myFile, line)) {
            if (currIndex == wordIndex) {
                word = line;
                break;
            }
            currIndex++;
        }
        myFile.close();
    }


    return word;
}


/*
Play Wordle
This function allows main to run the game.
*/
void PlayGame()
{
    string PlayerChoice;
    string Guess;

    bool playing = true;

    // main loop
    while (playing) {
        int currRow = 0;
        char** grid = CreateWordleGrid();
        int** colorGrid = CreateWordleColorGrid();

        string answer = ChooseWord();

        cout << "\n1. See Rules." << endl;
        cout << "\n2. Play the Game." << endl;
        cout << "\n3. Quit." << endl;
        cin  >> PlayerChoice;

        // game loop so the player can keep going until "3.Quit".
        do
        {
            if (!isdigit(PlayerChoice[0])) {
                cout << "Please enter a valid option (valid options are 1. See Rules, 2. Play the Game, 3. Quit)." << endl << endl;
                PlayerChoice[0] = '0';
                break;
            }

            // game states
            switch (PlayerChoice[0])
            {
            case '1':
                PlayerChoice = '3';
                GameRules();
                break;
            case '2':
            {
                PrintWordleGrid(grid, colorGrid);

                // Allows the player to know that they lost the game
                if (currRow == len) {
                    cout <<"\n" << "The Correct answer is: "<<answer << "!" << endl;
                    cout << endl << "Sorry, You did not guess the correct word. Try Again?" << endl << endl << endl;
                    PlayerChoice = '3';
                    break;
                }

                cout << "Enter word (5-letters): ";
                cin >> Guess;

                while (!IsValidWordle(Guess)) {
                    cout << "Please enter a word that contains 5 words." << endl;
                    cin >> Guess;
                }

                UpdateWordleGrid(grid, colorGrid, Guess, answer, currRow++);

                // if five 1's are present in colors grid, there are 5 characters which match, thus the game has been won
                int correctCharacterCount = 0;
                for (int i = 0; i < len; i++) {
                    correctCharacterCount += colorGrid[currRow - 1][i];
                }

                // win game. This makes the player aware if they won the game.
                if (correctCharacterCount == 5) {
                    PrintWordleGrid(grid, colorGrid);
                    cout << endl << "Magnificent!" << endl << endl << endl;
                    PlayerChoice = '3';
                }

                break;
            }
            case '3':
                cout << "Quit\n";
                playing = false;
                break;
            default:
                break;
            }
        } while (PlayerChoice[0] != '3');
    }
}


/*
Program entry point. Everything inserted into main with PlayGame();
*/
int main()
{
    cout << "Wordle ... " << endl;
    
    PlayGame();
    return 0;
}