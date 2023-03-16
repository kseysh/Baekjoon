#include<iostream>
#include<stack>
using namespace std;

int main() {
	int commandCount = 0;
	int stickHeight = 0;
	cin >> commandCount;
	stack<int> stickHeightStack;
	for (int i = 0; i < commandCount; i++) {
		cin >> stickHeight;
		stickHeightStack.push(stickHeight);
	}
	int compareValue = 0;
	int maxValue = 0;
	int count = 0;
	for (int i = 0; i < commandCount; i++) {
		compareValue = stickHeightStack.top();
		stickHeightStack.pop();
		if (compareValue > maxValue) {
			count++;
			maxValue = compareValue;
		}
	}
	cout << count;

	return 0;
}