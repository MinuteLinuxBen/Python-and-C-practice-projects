#include <iostream>
#include <iomanip>


using namespace std;

//Create a way to store objects for the game.
class MAGICBOX {




	//Creates the 3 x 3 array size for the inputed numbers in each column/row.
private:
	int LoSHUBox[3][3];

public:
	// MAGICBOX function allows for objects to be store and used in the squares for the game.
	MAGICBOX()


	{
		for (int x = 0; x < 3; x++)
		{
			for (int y = 0; y < 3; y++)
			{
				LoSHUBox[x][y] = 0;
			}
		}
	}
	// A means of taking valid numbers into the magic square. This can act as expection handling if the user

	// Function for inputing the square values 
	void ValueInsertion()

	{

		int RowValue;

		for (int x = 0; x < 3; x++)
		{

			for (int y = 0; y < 3; y++)
			{
				RowValue = 0;
				bool RepeatedValue;
				do {
					cout << "row: " << x + 1 << " Number: ";
					cin >> RowValue;
					// This accumlates 9 rows that will be used for the array 
					if (!(RowValue >= 1 && RowValue <= 9))
						cout << "Error ... Invalid number. Try again" << endl;

					// This is used to handle the user from using the same numbers twice within the game.
					RepeatedValue = check_for_repeats(RowValue);
					if (!RepeatedValue)
						cout << "Error ... " << RowValue << " is already in the Lo Shu Square. Try again" << endl;
				} while (!(RowValue >= 1 && RowValue <= 9 && RepeatedValue));

				LoSHUBox[x][y] = RowValue;
			}
		}
	}
	// Create a way to check for repeated values 
	bool check_for_repeats(int z) {
		// For loop allows iteration within the array 
		for (int x = 0; x < 3; x++)
		{

			for (int y = 0; y < 3; y++)
			{
				if (LoSHUBox[x][y] == z)
					//using a bool value of true/false allows for the user to see if they repeated something
					return false;
			}
		}
		// A given variable such as Z allows for the changes of the bool statement, so true is represented instead.
		return true;
	}

	// The square boxes are created with this function.
	void BuildASquare() {
		cout << endl;
		for (int x = 0; x < 3; x++)
		{
			cout << "\t-------------" << endl;
			cout << "\t|";
			
			for (int y = 0; y < 3; y++)
				
			{
				cout << " " << LoSHUBox[x][y] << " " << "|";
				
			}
			cout << endl;
			
		}
		cout << "\t-------------";
	}

	// method to check if the matrix is Lo Shu Magic Square
	bool EnsureLOSHU() {
		//Ensure that boxes can be filled with local variables in order 
		//accumlate numbers to build a 3 x 3 LoShu box.
		int DigOne = 0;
		int DigTwo = 0;
		int Total_Of_Row = 0;
		int TotalColumn = 0;


		// The first diagonal section of the 3 x 3 box is created
		for (int x = 0; x < 3; x++)
			DigOne += LoSHUBox[x][x];
		// Additonal diagonal section is made
		for (int x = 0, y = 2; x < 3 && y >= 0; x++, y--)
			DigTwo += LoSHUBox[x][y];

		//The two boxes should match. 
		if (DigOne != DigTwo)
			return false;

		// Total_Of_Row 
		for (int x = 0; x < 3; x++)
		{
			Total_Of_Row = 0;
			for (int y = 0; y < 3; y++)
			{
				// Accumulate the row totals for 
				Total_Of_Row += LoSHUBox[x][y];
			}
			// The rows must be equal for diagonal values to display evenly [3][3]
			if (Total_Of_Row != DigOne)
				return false;
		}

		// check for column totals
		for (int x = 0; x < 3; x++)
		{
			TotalColumn = 0;
			for (int y = 0; y < 3; y++)
			{
				// collect the TotalColumn
				TotalColumn += LoSHUBox[x][y];
			}
			// Column total is not equal to diagonal 1 or 2 and is used as a return type
			if (TotalColumn != DigOne)
				return false;
		}
		// if all condition goes false, return the bool value true
		return true;
	}

};

int main()
{
	char PlayAgain;
	

	do
	{
		cout << "\nCreating Lo Shu Square ... " << endl;
		cout << "\nEnter Nine Numbers (1-9)" << endl;

		// An object for MAGICBOX is created using 'ONE'.
		MAGICBOX One;

		One.ValueInsertion();
		//Include the function that allows the square to be created
		One.BuildASquare();

		cout << endl;
		//Ensure the user got a matching Lo Shu Magic Square box. 
		if (One.EnsureLOSHU())
			cout << "This is a Lo Shu Magic Square!!!";
		else
			cout << "Sorry ... This is not a Lo Shu Magic Square";



		cout << endl;
		cout << endl;
		//Create a do while loop to execute main and run the program over again until the user chooses "n && N" or "y" to keep playing. 
		cout << "Would you like to try again (y/n)? .\n" << endl;
		cin >> PlayAgain;


	} while (PlayAgain != 'n' && 'N');
	return 0;
}

		


