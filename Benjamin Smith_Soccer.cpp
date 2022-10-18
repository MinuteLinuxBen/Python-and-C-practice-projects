/*

Benjamin Smith
Socccer.cpp

4/25/2022

Instructions:

The team's information is loaded from a text file called "AtlantaUnited.txt".
Read in the file for data about the 11 players after the user is prompted to input the file name.
Option 2: The team's roster is displayed.
Option 3. Show a table that lists each player’s number, name, and points scored.
Option 4. Display team’s goals.
          Calaculation is done for the total goals scored by the entire team 
          The player(s) with the highest stats are shown
          The name of the player(s) who have earned the most points, along with the points earned is displayed.
Option 5. Quit.




*/
//HeaderFiles
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;


// Size to read from the txt file
const int SIZE = 11;


//Struct made to assign various data-types to the players
struct FootBall
{

    string PlayerName;

    int PlayerNumber;

    double ScorePlayer;

};


//Funtions prototypes

void displayTeamRoster(FootBall[], int);

double GoalsAdded (FootBall[], int);

int displayTeamStars(FootBall[], int);

void DataFromTeam(FootBall[], int&, string);


int
main()
{

    const int UploadFile = 1, List = 2, NumGoals = 3, MVP = 4, QUIT = 5;

    int choice;

    FootBall FootBallTeam[SIZE];

    int size;

    int total = 0;

    ifstream inFile;

    string FootBallFile;



    //Intro
    cout << "Soccer Team Goals..." << endl;


    //read data into array
    //getTeamData(soccerTeam, size);

    //Menu 
    do

    {

        //Simple interface menu to select 1 of 5 options 
        cout << "\nChoose one of the following options: " << endl
            << "\t1.Load team's information." << endl
            << "\t2.Display team's roster." << endl
            << "\t3.Display team's goal." << endl
            << "\t4.Display team's star(s)." << endl
            << "\t5.Quit." << endl;
        cout << "Option: ";
        cin >> choice;
        //Create a switch statement to allow the user to pick case statements: UploadFile, List, NumGoals, MVP,
        //and QUIT
        switch (choice)

        {

        case UploadFile:

            cout << "\nEnter file name: ";

            cin >> FootBallFile;
            //Open from the input value "FootBallFile".
            inFile.open(FootBallFile);

            DataFromTeam(FootBallTeam, size, FootBallFile);

            inFile.close();

            ;

            break;

        case List:

            displayTeamRoster(FootBallTeam, size);

            ;

            break;


        case NumGoals:

            total = GoalsAdded(FootBallTeam, size);

            cout << "Total goal scored: " << total << endl;

            ;

            break;


        case MVP:

            cout << "Top team player(s): ";

            displayTeamStars(FootBallTeam, size);

            ;

            break;


        case QUIT:

            cout << "\nSee you next season! ..." << endl;

            break;

        default:

            cout << "Error... Ivalid option.. Try again" << endl;

        }

    } while (choice != QUIT);

    return 0;

}

//Create a function prototype that read from the file added to the program
void DataFromTeam(FootBall arr[], int& size, string TheFile)
{

    ifstream inFile;

    //Open file
    inFile.open(TheFile);
    //Logic to prompt the user an incorrect file was placed into the program.
    if (!inFile)

    {
        //Test loop to keep bad or incorrect files from uploading
        cout << "this is a fatal error. coudl do not open the file" << endl;

        exit(EXIT_FAILURE);	// Function for exiting 
    }

    //Read from the file    
    size = 0;
    //Arrange the soccer players according the size of the array and name of player
    while (inFile >> arr[size].PlayerName)

    {

        inFile >> arr[size].PlayerNumber;

        inFile >> arr[size].ScorePlayer;

        size++;

        //close the file 
        inFile.close();

    }

}

//Function prototype to display the player's name, team number, and amount of goals scored
void displayTeamRoster(FootBall arr[], int size)
{

    cout << "\nPlayer Name \tNumber \tGoals";

    cout << "\n------------------------------" << endl;

    
    for (int x = 0; x < size; x++)

    {

        cout << arr[x].PlayerName << arr[x].PlayerNumber << arr[x].
            ScorePlayer << endl;

    }

}
//function prototypes to tally the goals made from the individual players
double GoalsAdded(FootBall arr[], int size)
{

    int total = 0;


    for (int x = 0; x < size; x++)

    {

        total += arr[x].ScorePlayer;

    }
    return total;

}

//Function Prototype to show the list of the team players
int displayTeamStars(FootBall arr[], int size)
{

    int highest = 0;

    int highestScore = arr[0].ScorePlayer;


    //Highest score totaled from a player
    for (int x = 1; x < size; x++)

    {

        if (arr[x].ScorePlayer > highestScore)


            highestScore = arr[x].ScorePlayer;

    }



    return 0;

}