/*

Ben Smith
4/4/2022

PaintEstimator.cpp
 
 input:
 User is prompted with the price of Paint
 Negative numbers or 0 won't be accpted for calculations

 User is prompted with the number of rooms needed to be painted
 Negative numbers or 0 won't be accpted for calculations

 User is prompted with the measurement in (square feet) based 
 on the size of the wall for each room

 Processing:
 1. Cost of one gallon of paint			Do/While Simply takes the gallon of paint and takes into account how much to charge the user if the 
										job requires more than one gallon to paint the specified rooms in the estimator.
 3. Number of room(s) painted			Do/While Loop is used over again to show that user needs to have a room greater than 25 square feet to be painted.
 4.	Paint cost for room(s):				float cal = float(sqrFeet) / float(GallonNeededToCoverArea);
 5. Labor cost:							double hours_for_work = (float(Footage_Square) / float(GallonNeededToCoverArea)) * 8;
 6. Total costs from each function:		double Cost_For_Painting = price + labor_cost;
  
 Output:
 Display to the user each category for the paint job estimator. 
 Gallons of paint used:
 Paint price:
 Hours of labor:
 Labor price:
 Total price for job:

*/

//Header Files
#include<iostream>
#include<iomanip>
#include<cstdlib>
#include<cmath>

using namespace std;

// Declare the prototypes for each functions
double getFour_Litre_Paint();
int getHouse_Rooms();
int EstWallSpace(int each_room);
void PaintEST(int sqrFoot, double pricePaint, int& gallons, double& cost);
void LaborEST(int Footage_Square, double& hours, double& cost);
void totalExpense(double& cost, double& labor_cost);

//Constants for the labor, paint, and hour(s)
#define GallonNeededToCoverArea 115
#define HourlyBasisOfLabor 25.00
#define LaborHours 8
int main()
{
	//Display the introduction title/name
	cout << "Welcome! AAA - Paint Job Estimator ..." << endl;
	double Gallon_Price_Cost = getFour_Litre_Paint();
	int Total_Rooms = getHouse_Rooms();
	int Coverage_Feet = EstWallSpace(Total_Rooms);
	int gallon;
	double cost;
	double hours, LABORcost;
	
	// Calling each function
	PaintEST(Coverage_Feet, Gallon_Price_Cost, gallon, cost);
	LaborEST(Coverage_Feet, hours, LABORcost);
	totalExpense(cost, LABORcost);
	return 0;
}

// This Function Gets the price of paint per gallon and uses a do/while loop
// Price of gallon is taken into account to be greater than or equal to zero.
double getFour_Litre_Paint() {
	double Gallon_Price_Accumlator;
	do {
		cout << "\nPrice per gallon of paint (>=0) : ";
		cin >> Gallon_Price_Accumlator;
	} while (Gallon_Price_Accumlator < 0);
	return Gallon_Price_Accumlator;
}

// get Number of rooms from the user
int getHouse_Rooms() {
	int House_rooms;
	do {
		cout << endl << "Number of rooms to be painted (>=1) : ";
		cin >> House_rooms;
	} while (House_rooms < 1);
	return House_rooms;
}
// calculate the square footage of each room from user.
int EstWallSpace(int each_room) {
	int squareft, sumSqrFtMust= 0;
	cout << endl << "Square feet of wall space (>=25)" << endl;
	for (int Accumlate = 1; Accumlate <= each_room; Accumlate++) {
		do {
			cout << "\tRoom " << Accumlate << ": ";
			cin >> squareft;
		} while (squareft < 25);
		sumSqrFtMust += squareft;
	}
	return sumSqrFtMust;
}

// calculate the paint cost to cover each room 
void PaintEST(int sqrFeet, double pricePaint, int& four_Litres, double& cost) {
	float cal = float(sqrFeet) / float(GallonNeededToCoverArea);
	four_Litres = ceil(cal);
	cout << endl << "\tPaint Job Estimate" << endl;
	cout << "_______________________________" << endl;
	cout << "Paint ..." << endl;
	cout << "Gallons of Paint: " << setw(8) << four_Litres << endl;
	cout << setprecision(2) << fixed;
	cost = pricePaint * four_Litres;
	cout << "Cost of Paint: " << setw(10) << "$ " << cost << endl;
	cout << "________________________________" << endl;
}

// calculate labor cost for paint job
void LaborEST(int Footage_Square, double& hours, double& lcost) {
	double hours_for_work = (float(Footage_Square) / float(GallonNeededToCoverArea)) * 8;
	cout << endl << "Labor for paint job ..." << endl;
	cout << setprecision(2) << fixed;
	cout << "Hours of Labor: " << setw(10) << hours_for_work << endl;
	lcost = hours_for_work * HourlyBasisOfLabor;
	cout << "Cost of Labor: " << setw(10) << "$ " << lcost << endl;
	cout << "_______________________________" << endl;
}

// calculate total cost that accounts from each function 
void totalExpense(double& price, double& labor_cost) {
	double Cost_For_Painting = price + labor_cost;
	cout << setprecision(2) << fixed;
	cout << endl << "Total Cost for paint job : " << setw(10) << "$ " << Cost_For_Painting << endl;
}



