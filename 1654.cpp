#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int k, n;
	cin >> k >> n;
	int cm;
	vector<int> v;
	for (int i = 0; i < k; i++) {
		cin >> cm;
		v.push_back(cm);
	}
	long long front = 1;
	long long rear = *max_element(v.begin(), v.end());
	long long mid = (front + rear) / 2;
	int result = 0;

	while (front <= rear) {
		int total = 0;
		mid = (front + rear) / 2;

		for (int i = 0; i < k; i++) {
			total += v[i] / mid;
			
		}


		if (total>=n) {
			front = mid + 1;
			if (result < mid) {
				result = mid;
			}
		}
		else {
			rear = mid - 1;
		}
	}

	cout << result;


	return 0;
}