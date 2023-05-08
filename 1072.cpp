#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	// ½Â·üÀÌ 99ÆÛ ÀÌ»óÀÌ¸é -1Ãâ·Â 
	long long x;
	long long y;
	cin >> x >> y;
	long long front = 1;
	long long rear = 1000000000;
	int result = -1;
	while (front <= rear) {
		int mid = (front + rear) / 2;
		if (100 * (y + mid) / (x + mid) > 100 * y / x) {
			rear = mid - 1;
			result = mid;
		}
		else {
			front = mid + 1;
		}
	}
	cout << result;
	return 0;
}