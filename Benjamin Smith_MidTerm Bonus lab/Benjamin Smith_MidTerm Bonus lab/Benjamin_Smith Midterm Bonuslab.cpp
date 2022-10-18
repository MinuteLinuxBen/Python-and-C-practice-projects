/*

	Ben Smith
	AssignmentGrade.cpp

	menu-driven interface program that allows the user to:
		1. Calculate assignment grade
		2. Display assignment grades
		3. Quit

	Input: user's choice
			Students' name, points recieved and maximum points.

	Processing: 1. Display menu
				2. prompt user for choice
				3. Dirve menu options
					case 1 // calculate grade
						  prompt user for student name, points recieved and maximum points
						  Calculate assignment grade
								gradePercent = ceil(pointsRecieved / maxPoints * 100);
						  Determine student student standing (gradePercent
							>= -> Excellent
							>= 80 && < 90 -> Well done
							>= 70 && <80 ->  good
							>= 60 && < 70 -> Needs improvement
							<60 -> Fail
						 Display students info <name, grade, standing>
						 Append record to "assignment.txt";
							open "assignments.txt" for appending
							Write students info <name, grade, standing> to file
							close file
					case 2 // Display file
						open "assignments.txt" for input
						While there are records in the file
							Read students info <name, grade, standing>
							Display record
						close file
					case 3 // quit
	Output: "assignment.txt" file containing assignment grades
			for students in a class
*/

//Header Files
#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{

	//Constants and variables
	const int CALCULATE = 1, DISPLAY = 2, QUIT = 3;
	int choice;
	string stdName;
	int aPoint, aMax;
	double gradePercent;
	fstream myFile;

	//Intro
	cout << "/nAssignment Calculator ... " << endl;
	//Set number formatting 
	cout << fixed << setprecision(0);

	//menu

	do
	{
		//Dispaly menu and prompt user for choice
		cout << "\nChoose one of the following options" << endl
			<< "\t1. Calculate assignment grade for one student." << endl
			<< "\t2. Display assignment grades" << endl
			<< "\t3. Quit." << endl
			<< "option: ";
		cin >> choice;
		//Drive menus options
		switch (choice)
		{
		case CALCULATE:
			//prompt user for student data

			//Determine standing 
			//Display student record
			//Append record to file
			;
			break;
		case DISPLAY:
			//Open file for input
			myFile.open("assignments.txt", ios::in);
			if (!myFile)
			{
				cout << "Error ... could not open file. Try again" << endl;
			}
			else
			{
				//while there are records
					//read record
					//display record
				// close file
				myFile.close();
			}

			break;
		case QUIT:
			cout << "\nGood bye ... " << endl;
			break;
		default:
			cout << "Error... Invalid option. Try again." << endl;


		}


	} while (choice != QUIT);



}