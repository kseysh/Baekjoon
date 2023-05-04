#include<iostream>
#include<algorithm>
using namespace std;

int arr[100001];
int n;

bool find(int data) {
	int front = 0;
	int rear = n - 1;
	int mid = (n - 1) / 2;
	while (front <= rear) {
		mid = (front + rear) / 2;
		if (arr[mid] == data) {
			return true;
		}
		else if (arr[mid] > data) {
			rear = mid-1;
		}
		else if (arr[mid] < data) {
			front = mid+1;
		}
	}
	return false;
}

int main() {
	ios::sync_with_stdio(0); 
	cout.tie(0);
	cin.tie(0);
	int m;
	int x;
	int data;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x;
		arr[i] = x;
	}
	sort(arr,arr + n);
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> data;
		if (find(data)) {
			cout << 1 << '\n';
		}
		else {
			cout << 0 << '\n';
		}
	}


	return 0;
}