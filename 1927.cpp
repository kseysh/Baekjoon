#include<iostream>
#include<vector>
using namespace std;
class unsortedPQ {
public:
	vector<int> seq;
	void insert(int i) {
		seq.push_back(i);
	}
	int removeMin(vector<int>& v) {
		int minVal = 10000;
		int minIdx = -1;
		for (int i = 0; i < v.size(); i++) {
			if (minVal > v[i]) {
				minVal = v[i];
				minIdx = i;
			}
		}
		v.erase(v.begin() + minIdx);
		return minVal;
	}
	void selectionSort() {
		vector<int> pq;
		int size = seq.size();
		for (int i = 0; i < size; i++) {
			pq.push_back(seq.back());
			seq.pop_back();
		}
		for (int i = 0; i < size; i++) {
			seq.push_back(removeMin(pq));
		}
	}
};

int main() {
	int N;
	int x;
	cin >> N;
	unsortedPQ pq;
	for (int i = 0; i < N; i++) {
		cin >> x;
		pq.insert(x);
	}
	pq.selectionSort();
	for (int i = 0; i < N; i++) {
		cout << pq.seq[i] << endl;
	}

	return 0;
}