#include <iostream>
using namespace std;

int main() {
	while (true) {
		int a, b = 0;
		cin >> a >> b;
		if (a == 0 && b == 0) {
			break;
		}
		cout << a + b << endl;

	}

	return 0;
}