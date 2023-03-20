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
		cout << underbarMaker(currentCount) << "\"재귀함수가 뭔가요?\"" << endl;
		cout << underbarMaker(currentCount) << "\"재귀함수는 자기 자신을 호출하는 함수라네\"" << endl;
		cout << underbarMaker(currentCount) << "라고 답변하였지." << endl;

		return;

	}

	cout << underbarMaker(currentCount) <<"\"재귀함수가 뭔가요?\"" << endl;
	cout << underbarMaker(currentCount) << "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어." << endl;
	cout << underbarMaker(currentCount) << "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지." << endl;
	cout << underbarMaker(currentCount) << "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"" << endl;
	recursionFunction(recursionCount, ++currentCount);
	cout << underbarMaker(--currentCount)<<"라고 답변하였지." << endl;
}

int main() {
	int commandCount = 0;
	int currentCount = 0;
	cin >> commandCount;
	cout << "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다." << endl;
	recursionFunction(commandCount,currentCount);


	return 0;
}