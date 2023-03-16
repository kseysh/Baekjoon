#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	int count = 0;
	stack<string> stack;
	string inputSentence = "";
	string inputString = "";
	cin >> count;
	cin.ignore();
	for (int i = 0; i < count; i++) {
		getline(cin, inputSentence);
		for (int j = 0; j < inputSentence.length(); j++) {
			if (inputSentence[j] == ' ') {
				stack.push(inputString);
				inputString = "";
			}
			else if (j == inputSentence.length() - 1) {
				inputString += inputSentence[j];
				stack.push(inputString);
				inputString = "";
			}
			else {
				inputString += inputSentence[j];
			}
		}
		inputSentence = "";
		int stackSize = stack.size();
		cout << "Case #" << i + 1 << ":";
		for (int k = 0; k < stackSize; k++) {
			cout << " " << stack.top();
			stack.pop();
		}
		cout << endl;
	}


	return 0;
}