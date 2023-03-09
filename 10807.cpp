#include<iostream>
using namespace std;

int main() {
	int inputCount = 0;
	cin >> inputCount;
	int *numberArray;
	int target = 0;
	int targetFindCount = 0;
	numberArray = new int[inputCount];
	for (int i = 0; i < inputCount; i++) {
		cin >> numberArray[i];
	}
	cin >> target;
	for (int i = 0; i < inputCount; i++) {

		if (numberArray[i] == target) {
			targetFindCount++;
		}
	}

	cout << targetFindCount;

	return 0;

	// count 함수를 사용하여 원소 확인 가능
}