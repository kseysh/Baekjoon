#include <iostream>
using namespace std;

int main() {
	int number = 0;
	cin >> number;
	string oxString = "";
	int sum = 0;
	for (int i = 0; i < number; i++) {
		int plusScore = 0;
		cin >> oxString;
		int oxStringLength = oxString.length();
		for (int i = 0; i < oxStringLength; i++) {
			if (oxString[i] == 'O') {
				sum += 1 + plusScore;
				plusScore += 1;
			}
			else {
				plusScore = 0;
			}
		}
		cout << sum << endl;
		sum = 0;
	}

	return 0;
}