#include <iostream>
using namespace std;

int main() {
	string str = "";
	for (int i = 0; i < 8; i++) {
		char a = 'a';
		cin >> a;
		str += a;
	}
	if (str == "12345678") {
		cout << "ascending" << endl;
	}
	else if (str == "87654321") {
		cout << "descending" << endl;
	}
	else {
		cout << "mixed" << endl;
	}

	return 0;
}