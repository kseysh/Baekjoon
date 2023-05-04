#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	vector<int> trees;
	int n, m, height;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> height;
		trees.push_back(height);
	}
	int front = 0;
	int rear = *max_element(trees.begin(), trees.end());
	int mid = (front + rear) / 2;
	int result = 0;

	while (front <= rear) {
		long long int total = 0;
		mid = (front + rear) / 2;
		for (int i = 0; i < n; i++) {
			if (trees[i] > mid) {
				total += trees[i] - mid;
			}
		}
		if (total >= m) {
			result = mid;
			
			front = mid + 1;
		}
		else {
			rear = mid - 1;
		}
	}
	cout << result;

	return 0;
}