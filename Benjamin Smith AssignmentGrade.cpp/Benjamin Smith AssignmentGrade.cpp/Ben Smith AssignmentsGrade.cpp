
#include<iostream>
#include<fstream>
#include<iomanip>
#include<math.h>

using namespace std;

// menu method to show all the available menu to the user
// and get user choice and returns it
int menu() {
    cout << "1. Calculate assignment grade for one student.\n";
    cout << "2. Display assignment grades.\n";
    cout << "3. Quit.\n";
    cout << "Enter your choice: ";
    int choice;
    cin >> choice;
    return choice;
}

// take student name,score and total
// and calculate its percentage and display complement
void getInput() {
    string name;
    double score;
    double total;
    ofstream file("assignment.txt", ios_base::app);

    //clear the buffer
    string temp;
    getline(cin, temp);

    //take user input
    cout << "\nStudent Name: ";
    getline(cin, name);
    cout << "Student Score (0-100): ";
    cin >> score;
    cout << "Assignment total points(0-100): ";
    cin >> total;

    //calculate percentage
    double per = (score / total) * 100;
    per = ceil(per);


    // take complement
    // based on student percentage
    string comp;

    if (per >= 90) {
        comp = "Excellent";
    }
    else if (per >= 80) {
        comp = "Well Done";
    }
    else if (per >= 70) {
        comp = "Good";
    }
    else if (per >= 60) {
        comp = "Need Improvement";
    }
    else {
        comp = "Fail";
    }

    //print the student percentage and complement
    cout << "\n\nAssignment Calculator\n";
    cout << "----------------------------------\n";
    cout << setw(20) << left << name << setw(3) << right << per << "%" << setw(15) << right << comp << endl;

    // write student record to file
    file << setw(20) << left << name << setw(3) << right << per << "%" << setw(15) << right << comp << endl;
    file.close();
}


// display the content of the file
void display() {
    ifstream file("assignment.txt");
    string str;
    cout << "\n\nStudent Assignment Score\n";
    cout << "--------------------------------\n";
    while (getline(file, str)) {
        cout << str << endl;
    }
    cout << endl << endl;
    file.close();
}

int main() {

    // variable to take user choice
    int choice;
    while (true) {

        // show menu
        choice = menu();

        // if choice is 3 break from the program
        if (choice == 3) break;

        // if coice is 1
        // take user input
        if (choice == 1) {
            getInput();
        }
        // if choice is 2 show the file content
        else if (choice == 2) {
            display();
        }
        // if choice is invalid
        else {
            cout << "\nWrong choice Entered...\n";
        }
        cout << endl;
    }
    return 0;
}