#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {

	ios::sync_with_stdio(0);
	cin.tie(0);

	int m, n, data;
	vector<int> v;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> data;
		v.push_back(data);
	}
	long long front = *max_element(v.begin(), v.end());
	long long rear = 1000000000;

	while (front <= rear) {
		long long mid = (front + rear) / 2;
		long long total = 0;
		long long blueCount = 1;
		for (int i = 0; i < n; i++) {
			if (v[i] > mid) {
				break;
			}
			if (mid >= total + v[i]) {
				total += v[i];
			}
			else {
				total = v[i];
				blueCount++;
			}
		}

		if (blueCount > m) {
			front = mid + 1;
		}
		else {
			rear = mid - 1;
		}

	}
	cout << front;



	return 0;
}