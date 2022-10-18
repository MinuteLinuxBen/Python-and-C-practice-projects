#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
	fstream myFile;
	myFile.open("STUDENT.txt", ios::in);
	if (myFile.is_open()) {
		string line;
		while (getline(myFile, line)) {
			cout << line << endl;
		}
		myFile.close();
	}
	
	
		
return 0;
}