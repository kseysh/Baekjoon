#include <iostream>
using namespace std;

int main() {
	int number = 0;
	cin >> number;
	for (int i = 0; i < number; i++) {
		int a, b;
		cin >> a >> b;
		cout << a + b << endl;
	}

	return 0;
}