#include <iostream>
using namespace std;


int main() {
	int a, b = 0;
	cin >> a >> b;
	int bigValue,smallValue = 0;
	if (a >= b) {
		bigValue = a;
		smallValue = b;
	}
	else {
		bigValue = b;
		smallValue = a;
	}
	int greatestMultiple = smallValue;
	for (int i = 1; i < smallValue+1; i++) {
		if (bigValue % i == 0 && smallValue % i == 0) {
			greatestMultiple = i;
		}
	}
	cout << greatestMultiple << endl;

	int divisorMultiplySum = 1;
	int count = 2;
	count = 1;
	while (true) {
		if (smallValue * count % bigValue == 0) {
			cout << smallValue * count;
			break;
		}
		count++;
	}
	return 0;
}