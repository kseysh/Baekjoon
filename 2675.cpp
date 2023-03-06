#include <iostream>
using namespace std;

int main() {
	int number = 0;
	int repeatNumber = 0;
	string str = "";
	cin >> number;
	for (int i = 0; i < number; i++) {
		string newString = "";
		cin >> repeatNumber >> str;
		int stringLength = str.length();
		for (int i = 0; i < stringLength; i++) {
			for (int j = 0; j < repeatNumber; j++) {
				newString += str[i];
			}
		}
		cout << newString << endl;
	}

	return 0;
}