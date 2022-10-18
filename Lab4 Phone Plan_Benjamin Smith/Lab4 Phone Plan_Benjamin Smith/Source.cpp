/*
Benjamin Smith
2/21/2022

iMobile.cpp

The purpose of this program is to quote certain phone plans from a menu structure.
	1. The user must choose 1 of 3 phone packages 
	2. Phone plans are flat rate and should be defined as a constant
	3. The gigabyte usage will of course vary based on the phone plan selected.
	4. Plan 1. Is $39.99 a month with 4 gigabytes of data. Additional gigabytes are $10 each.
	5. Plan 2. Is $59.99 a month with 8 gigabytes of data. Additional gigabytes are $5 each.
	6. plan 3. Is $69.99 a month with unlimited data/gigabyte use. 
	7. Define/declare constants.
	8. Define/declare doubles.
	9. Define/declare float.
	10. Define/declare char.
	11. Prompt user for packages 1-3
	12. Prompt user for gigabyte usage. This is important if they should go over without an unlimited plan.
	13. Create calculations based on monthly plans selected, allotment of gigabytes, total amount due for using plans 1-3. 
	14. If the the number entered does not match 1-3 it will not make the case and will direct the user to the default portion 
	giving the user an error that they need to pick a listed choice for one of the plans.
	15. The if/else structure is also based off of gigabytes used for 2 out of the 3 phone plans. 
	Customers will be charged according to data usage.
	16. The user will also be given an error depending on the gigabytes entered. The values can only be positve. 

*/


#include<iostream>
#include<iomanip>

using namespace std;

int main()

{
	//The prices should be defined by constants in "double" if they are represented with additional change.
	//Using the numbers of actual prices is optional.

	// price of package A
	double plan_one_monthly = 39.99;
	//price of package B
	double plan_two_monthly = 59.99;
	//price of package C
	double plan_three_monthly = 69.99;

	//gigabytes that are extra or intergral to phone plan
	const int gig_four = 4;
	const int gig_eight = 8;
	const int gig_diez = 10;
	const int gig_five = 5;
	//The amount left over from the phone plan.
	const int left_over = 0;

	// The monthly rate and gigabytes of the plan used depending on the package picked by the customer/user.
	int monthly_plan;

	// The plan's associated prices and gig restrictions.
	float a_price_plan, b_price_plan, c_price_plan;


	// The char is the package the customer picks as one of their options.
	char package, bad_data;

	//The customer/user is greeted with the name of the service and is prompted with selecting a package (1-3)
	cout << "iMobile Bill Calculator...\n\n";
	cout << "Select a subscription package:\n";
	cout << "\t1. Package A\n";
	cout << "\t2. Package B\n";
	cout << "\t3. Package C\n";

	cout << "Package: ";
	cin >> package;

	cout << "\nHow many gigabytes of data were used: " << endl;
	cin >> monthly_plan;

	if (monthly_plan < 0) {
		cout << "Error ... Invalid gigabytes entered. Try again." << endl;
		return 0;
	}

	// if/else selection structure is based off of these calculations and comparisons.

	if ((monthly_plan - gig_four) > left_over)

		a_price_plan = plan_one_monthly + (monthly_plan - gig_four) * gig_diez;

	else

		a_price_plan = plan_one_monthly;


	if (monthly_plan - gig_eight > left_over)

		b_price_plan = plan_two_monthly + ((monthly_plan - gig_eight) * gig_five);

	else

		b_price_plan = plan_two_monthly;

	c_price_plan = plan_three_monthly;

	// A switch statement is used in this case because the packages selected provide different requirements such as cost and the gig allotment that comes with the associated fees.




	switch (package) {

	case '1':

		cout << "\nThe total amount due is $" << a_price_plan << endl;

		break;

	case '2':

		cout << "\nThe total amount due is $" << b_price_plan << endl;

		break;

	case '3':

		cout << "\nThe total amount due is $" << c_price_plan << endl;

		break;

	default:

		cout << "Error... Invalid package. Try again. " << endl;


	}



	return 0;

}
