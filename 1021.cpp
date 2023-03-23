#include<iostream>
using namespace std;

struct node {
	int data;
	node* next;
	node* prev;
};

class listQueue {
public:
	listQueue();
	bool empty();
	int size();
	int front();
	int back();
	void enqueue_front(int data);
	void enqueue_back(int data);
	int dequeue_front();
	int dequeue_back();
	void print();
	void moveLeft();
	void moveRight();
	int findTargetIndex(int target);
	void makeQueue(int count);

	node* header;
	node* frontNode;
	node* rearNode;
	int queueSize; //큐의 크기를 저장하는 변수
	node* trailer;
	int count;
};

listQueue::listQueue() {
	frontNode = NULL;
	rearNode = NULL;
	header = new node;
	trailer = new node;
	queueSize = 0;
	count = 0;
}
bool listQueue::empty() {
	return (queueSize == 0);
}
int listQueue::size() {
	return queueSize;
}
int listQueue::front() {
	if (empty()) {
		cout << "empty" << endl;
		return -1;
	}
	else {
		return frontNode->data;
	}
}
int listQueue::back() {
	if (empty()) {
		cout << "empty" << endl;
		return -1;
	}
	else {
		return rearNode->data;
	}
}
void listQueue::enqueue_front(int data) {
	node* newNode = new node;
	newNode->data = data;
	if (empty()) {
		frontNode = rearNode = newNode;

		header->next = frontNode;
		trailer->prev = rearNode;
	}
	else {
		newNode->next = frontNode;
		newNode->prev = header;
		header->next = newNode;
		frontNode->prev = newNode;
		frontNode = newNode;
	}
	queueSize++;
}
void listQueue::enqueue_back(int data) {
	node* newNode = new node;
	newNode->data = data;
	if (empty()) {
		frontNode = rearNode = newNode;
		header->next = frontNode;
		frontNode->prev = header;
		rearNode->next = trailer;
		trailer->prev = rearNode;
	}
	else {
		rearNode->next = newNode;
		newNode->next = trailer;
		trailer->prev = newNode;
		newNode->prev = rearNode;
		rearNode = newNode;
	}
	queueSize++;
}
int listQueue::dequeue_front() {
	int data = frontNode->data;
	if (empty()) {
		cout << "empty" << endl;
		return -1;
	}
	node* curNode = frontNode;
	if (size() == 1) {
		frontNode = rearNode = NULL;
	}
	else {
		header->next = frontNode->next;
		frontNode->next->prev = header;
		frontNode = frontNode->next;
	}
	delete curNode;
	queueSize--;
	return data;
}
int listQueue::dequeue_back() {
	int data = rearNode->data;
	if (empty()) {
		cout << "empty" << endl;
		return -1;
	}
	node* curNode = rearNode;
	if (size() == 1) {
		frontNode = rearNode = NULL;
	}
	else {
		rearNode->prev->next = trailer;
		trailer->prev = rearNode->prev;
		rearNode = rearNode->prev;
	}
	delete curNode;
	queueSize--;
	return data;
}
void listQueue::print() {
	node* curNode = header->next;
	if (empty()) {
		cout << "empty" << endl;
		return;
	}
	else {
		for (int i = 0; i < queueSize; i++) {
			cout << curNode->data << ' ';
			curNode = curNode->next;
		}
		cout << endl;
	}

}

void listQueue::moveLeft() {
	enqueue_back(dequeue_front());
}
void listQueue::moveRight() {
	enqueue_front(dequeue_back());
}

void listQueue::makeQueue(int count) {
	for (int i = 0; i < count; i++) {
		enqueue_back(i+1);
	}
}

int listQueue::findTargetIndex(int target) {
	node* curnode = header->next;
	int countIndex = 0;
	for (int i = 0; i < queueSize; i++) {
		countIndex++;
		if (curnode->data == target) {
			return countIndex;
		}
		else {
			curnode = curnode->next;
		}
	}
	return -1;
}






int main() {
	int queueSize = 0;
	int popCount = 0;
	int moveCount = 0;
	int popTarget = 0;
	int targetIndex = 0;
	int inputValue = 0;
	listQueue queue;
	cin >> queueSize >> popCount; // 순서 확인하기
	queue.makeQueue(queueSize);
	for (int i = 0; i < popCount; i++) {
		cin >> popTarget;
		targetIndex = queue.findTargetIndex(popTarget);
		if (targetIndex - 1 < queue.queueSize - targetIndex + 1) {
			for (int i = 1; i < targetIndex; i++) {
				queue.moveLeft();
				moveCount++;
			}

			queue.dequeue_front();
		}
		else {
			for (int i = 0; i < queue.queueSize - targetIndex + 1; i++) {
				queue.moveRight();
				moveCount++;
			}
			queue.dequeue_front();
		}

	}

	cout << moveCount;

	return 0;
}