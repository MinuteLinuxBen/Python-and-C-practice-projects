#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
	// setting the precision to two decimal places
	std::cout << std::setprecision(1) << std::fixed;

	// Declaring variables
	ifstream dataIn;
	int Text, count = 0;
	string minName, maxName;
	double sum = 0.0, avg = 0.0;
	int min = 9999, max = -9999;
	string name, str;
	int score;
	string myFile, description, profName, term;
	cout << "Course Summary App ..." << endl;

	/* This while loop continues to execute
	* until the user enters a valid choice or choice is 2
	*/
	while (true)
	{
		// displaying the menu
		cout << "\nChoose one of the following options" << endl;
		cout << "\t1. Process Grades Summary report." << endl;
		cout << "\t2. Quit." << endl;

		// getting the choice entered by the user
		cout << "Option: ";
		cin >> myFile;

		// Based on the user choice the corresponding case will be executed
		switch (myFile)
		{
		case 1:
		{

			cout << "\nGrades Summary Report ..." << endl;
			// Reading the filename entered by the user
			cout << "Enter name of the file: ";
			cin >> Text;

			//OPEN FILE
			myFile.open("Text.txt"), ios::out);
			/*
			* checking whether the file name is valid or not
			*/
			if (dataIn.fail())
			{
				cout << "** File Not Found **";
				return 1;
			}
			else
			{
				// Reading the data from the file
				getline(dataIn, description);
				getline(dataIn, profName);
				getline(dataIn, term);
				cout << "\n------------------------------------------------------" << endl;
				cout << "\n" << description << endl;
				cout << "\n" << profName << setw(40) << right << term << endl;
				cout << "\nList of Students" << endl;
				cout << "------------------------------------------------------" << endl;

				/*
				* Reading the data from the file
				*/
				while (getline(dataIn, name))
				{
					getline(dataIn, str);
					score = atoi(str.c_str());
					if (min > score)
					{
						min = score;
						minName = name;
					}
					if (max < score)
					{
						max = score;
						maxName = name;
					}
					sum += score;
					count++;
					cout << setw(40) << left << name << setw(20) << left << score << endl;
				}
				/*
				* closing the file
				*/
				dataIn.close();

				avg = sum / count;

				// Displaying the output
				cout << "Highest Grade: " << maxName << " - " << max << endl;
				cout << "Lowest Grade: " << minName << " - " << min << endl;
				cout << "Average Grade: " << avg << endl;
			}
			continue;
		}
		case 2:
		{
			cout << "\nGood Bye ..." << endl;
			break;
		}
		default:
		{
			cout << "** Invalid CHoice **" << endl;
			continue;
		}
		}
		break;
	}


	return 0;
}