#include<iostream>
using namespace std;
string underbarMaker(int currentCount) {
	string underbar = "";
	for (int i = 0; i < currentCount; i++) {
		underbar += "____";
	}
	return underbar;
}
void recursionFunction(int recursionCount, int currentCount) {
	if (recursionCount == currentCount) {
		cout << underbarMaker(currentCount) << "\"����Լ��� ������?\"" << endl;
		cout << underbarMaker(currentCount) << "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"" << endl;
		cout << underbarMaker(currentCount) << "��� �亯�Ͽ���." << endl;

		return;

	}

	cout << underbarMaker(currentCount) <<"\"����Լ��� ������?\"" << endl;
	cout << underbarMaker(currentCount) << "\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���." << endl;
	cout << underbarMaker(currentCount) << "���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���." << endl;
	cout << underbarMaker(currentCount) << "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"" << endl;
	recursionFunction(recursionCount, ++currentCount);
	cout << underbarMaker(--currentCount)<<"��� �亯�Ͽ���." << endl;
}

int main() {
	int commandCount = 0;
	int currentCount = 0;
	cin >> commandCount;
	cout << "��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������." << endl;
	recursionFunction(commandCount,currentCount);


	return 0;
}