#include<iostream>
using namespace std;

struct Node {
	int data;
	struct Node* next;
};

class circleList {
public:
	circleList();
	void append(int data);
	void deletion(int n, int k);
private:
	Node* head;
	Node* tail;
	int listSize;
};

circleList::circleList() {
	head = NULL;
	tail = NULL;
	listSize = 0;
}

void circleList::append(int data) {
	Node* newNode = new Node;
	newNode->data = data;

	if (this->listSize == 0) {
		tail = head = newNode;
		head->next = tail->next = newNode;
	}
	else {
		tail->next = newNode;
		newNode->next = head;
		tail = newNode;
	}

	this->listSize++;
}

void circleList::deletion(int n, int k) {
	Node* preNode = head;
	Node* delNode = head;
	int count = 1;
	int* outputList = new int[n](); // 크기 k로 동적 할당하고 0으로 초기화
	int outputListIndex = 0;
	while (true) {

		if (listSize == 0) {
			break;
		}
		else if (count % k == 0) {
			outputList[outputListIndex] = delNode->data;
			outputListIndex++;
			preNode->next = delNode->next;
			delNode = preNode->next;
			listSize--;
		}
		else {
			preNode = delNode;
			delNode = preNode->next;
		}

		count++;
	}

	cout << '<';
	for (int i = 0; i < n; i++) { // n으로 수정
		cout << outputList[i];
		if (i != n - 1) { // 마지막 값 이후에는 ',' 출력하지 않도록 수정
			cout << ", ";
		}
	}
	cout << '>';
	delete[] outputList; // 동적 할당한 메모리 반환
}

int main() {
	int n, k;
	cin >> n >> k;
	circleList c;
	for (int i = 1; i <= n; i++) {
		c.append(i);
	}
	c.deletion(n, k);
	return 0;
}