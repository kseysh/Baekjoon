#include<iostream>
#include<stack>
using namespace std;

int main() {
	int book = 0;
	int dummy = 0;
	int k = 0;
	int inputValue = 0;
	cin >> book >> dummy;
	int** array = new int*[dummy];


	for (int i = 0; i < dummy; i++) {
		cin >> k;
		int* tempArray = new int[k];
		for (int j = 0; j < k; j++) {
			cin >> inputValue;
			tempArray[j]=inputValue;
		}
		array[i] = tempArray;
	}

	for (int i = 1; i < book+1; i++) {
		for (int j = 0; j < dummy; j++) {
			int a = array[j].length() - 1;
			if(array[j][])
		}
	}
	cout << "Yes";

	return 0;
}