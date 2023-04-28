#include<iostream>
#include<vector>
using namespace std;

class sortedPQ {
public:
	vector<int> seq;
	void insert(int data) {
		seq.push_back(data);
	}
	void insertion(int data,vector<int>& v) {
		int maxIdx = 0;
		for (int i = v.size()-1; i >= 0; i--) {
			if (v[i] < data) {
				maxIdx = i+1;
				break;
			}
		}
		v.insert(v.begin() + maxIdx,data);
	}
	void insertionSort() {
		int size = seq.size();
		vector<int> pq;
		for (int i = 0; i < size; i++) {
			int data = seq.back();
			seq.pop_back();
			insertion(data, pq);
		}
		for (int i = 0; i < size; i++) {
			seq.push_back(pq.back());
			pq.pop_back();
		}
	}

	int top() {
		if (seq.size() == 0) {
			return -1;
		}
		return seq[0];
	}

	void print() {
		for (int i = 0; i < seq.size(); i++) {
			cout << seq[i] << " ";
		}
		cout << endl;
	}
};

int main() {
	int peopleCount = 0;
	int dasomVoteCount = 0;
	int badpeople = 0;
	int voteCount;
	sortedPQ pq;
	cin >> peopleCount;
	cin >> dasomVoteCount;
	for (int i = 0; i < peopleCount-1; i++) {
		cin >> voteCount;
		pq.insert(voteCount);
	}
	pq.insertionSort();
	while (pq.top() >= dasomVoteCount) {
		pq.seq[0] = pq.seq[0] - 1;
		pq.insertionSort();
		badpeople++;
		dasomVoteCount++;
	}
	cout << badpeople;

	return 0;
}