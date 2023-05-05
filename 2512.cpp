#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;


int main() {
	vector<int> moneyCall;
	int n, money;
	cin >> n;//������ ��
	for (int i = 0; i < n; i++) {
		cin >> money;// �����û
		moneyCall.push_back(money);
	}
	long long budget;
	cin >> budget;//  �� ����
	int front = 1;
	int rear = *max_element(moneyCall.begin(), moneyCall.end());
	int mid;
	int result = 0;
	while (front <= rear) {
		int total = 0;
		mid = (front + rear) / 2;
		for (int j = 0; j < n; j++) {
			if (moneyCall[j] <= mid) {
				total += moneyCall[j];
			}
			else {
				total += mid;
			}
		}
		if (total > budget) {
			rear = mid - 1;
		}
		else {
			if (mid > result) {
				result = mid;
			}
			front = mid + 1;
		}
	}
	cout << result;


	return 0;
}
