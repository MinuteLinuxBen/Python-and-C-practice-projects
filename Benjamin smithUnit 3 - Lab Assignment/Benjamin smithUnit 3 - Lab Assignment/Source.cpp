/*
Benjamin Smith
2 / 9 / 2022
LoanCalculator.cpp

The purpose of this program is to prompt the user for the loan amount they would like to borrow,
annual interest rate, and term of the loan expressed(in years) that it takes to pay off.The loan calculator
displays the expected monthly payment.
Total amount to be paid, and total interest rate is displayed along with the loan amount.

Input: Name of user, Loan Amount($), Annual Interest Rate(%), term of loans expressed in(years), and Date of Report if manually inputed.

Processingand Calculations : 1. prompt user for name.
2. prompt user for loan amount.
3. Asign the interest rate for the loan
4. Calculate the total amount years it will take to pay off the loan.
5. Display the loan amount in the output section "Loan payment summary report."
6. To achieve the montly interest rate divide the annual interest rate by the 12 months out of the year.
7. Display how many payments in months it will take to fulfill(x) amount of years in the fixed rate of the loan.
8. Include monthly payments.This is done from taking the monthly interest rate and including it to the total cost for each month.
e.g. 360 months into 30 years will produce $550 a month.
Don't forget monthly interest calculated.
9. Take the accumlation of interest and add it to the amount originally borrowed for the loan.
10. Lastly, subtract your original amount borrowed from the interested accumlated from the(x) amount of years paid.
e.g.original money borrowed : $12, 000. Total amount after interest on loan for
30 years @ 3.75 % annually: $20, 0065.94.
loan borrowed plus annual interest after 30 years $20, 0065.94 - loan borrowed $12, 000.00 = $8, 0065.94
Total interest = $8, 0065.94.

Output : Report the loan amount including the annual and monthly interest rate.Display the months needed to pay the loan, monthly payment amount,
with the total amount plus the total interest from the entire loan.

*/


//Header files
#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main()
{


	//declaring variables, Integers, and Strings.
	string name, date_in_report;
	const int Months_Of_Year = 12, Interest_Rate = 1200;
	double amount, interest, term_of_loan, monthly_Interest_Rate, totalAmountToPay, totalInterest,
		numberOfPayment, monthlyPayment;

	//Prompt user and read input.

	cout << "Loan Payment Calculator..." << endl;
	cout << "\n\Please Enter the Following Information:" << endl;
	cout << left << setw(30) << "\n\Borrower's name: ";
	getline(cin, name);
	cout << "Loaning Institution:\t" << "Davie Banks & Loan" << endl;
	cout << "\n";
	cout << left << setw(30) << "Loan amount($): ";
	cin >> amount;
	cout << left << setw(30) << "Annual interest rate: ";
	cin >> interest;
	cout << left << setw(30) << "Term of Loan(Years): ";
	cin >> term_of_loan;
	cout << "\n";
	cout << left << setw(30) << "Date of report: ";
	cin.ignore();
	getline(cin, date_in_report);

	//Include all calculations in processing steps. 

	//1.) The agreed Interest rate is divided up into the amount of months that make up a year.
	monthly_Interest_Rate = interest / Interest_Rate;

	//2.)calculating number of Payments is done by taking the years of the and multiplying it by the 12 months of the year.
	numberOfPayment = term_of_loan * Months_Of_Year;

	//3.)calculate the Monthly payment using a determined formula. Simply convert this formula for the compiler so the code can properly execute.
	monthlyPayment = monthly_Interest_Rate * pow((1 + monthly_Interest_Rate), numberOfPayment) * amount / (pow((1 + monthly_Interest_Rate), numberOfPayment) - 1);

	// 4.) The Total amount paid is calculated from the determined monthly payment. 
		   //Multiply it by the calculated number of payments for the fixed loan.
	totalAmountToPay = monthlyPayment * numberOfPayment;


	// 5.) Calculate the difference in total interest by taking the accumulated amount 
		  //and subtracting it from the original cost of the desired money borrowed for the loan.
	totalInterest = totalAmountToPay - amount;


	cout << "----------------------------------------------------" << endl;
	cout << fixed << setprecision(2);
	//displaying the results from calculations and user's input
	cout << "Loan Payment Summery Report" << endl;
	cout << "\n" << left << setw(40) << "Davie Bank & Loan" << name << endl;
	cout << "Annual Interest Rate: " << interest << "%" << endl;
	cout << "Date: " << date_in_report << endl;
	cout << "\n";
	cout << left << setw(40) << "Loan Amount: " << "$ " << right << setw(12) << amount << endl;
	cout << left << setw(42) << "Monthly interest rate: " << right << setw(11) << (monthly_Interest_Rate) * 100 << "%" << endl;
	cout << left << setw(42) << "Number of payments: " << right << setw(12) << numberOfPayment << endl;
	cout << left << setw(40) << "Monthly payment: " << "$ " << right << setw(12) << monthlyPayment << endl;
	cout << "\n";
	cout << left << setw(40) << "Total amount to pay: " << "$ " << right << setw(12) << totalAmountToPay << endl;
	cout << left << setw(40) << "Total Interest: " << "$ " << right << setw(12) << totalInterest << endl;
	cout << "\n\-----------------------------------------------------" << endl;

	return 0;
}