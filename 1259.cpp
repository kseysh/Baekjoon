#include <iostream>
using namespace std;

int main() {
	string inputValue = "";
	
	while (true) {
		int yesOrNo = 0;
		cin >> inputValue;
		int stringLength = inputValue.length();
		if (inputValue == "0") {
			break;
		}
		for (int i = 0; i < stringLength/2; i ++) {
			if (inputValue[i] != inputValue[stringLength - 1 - i]) {
				yesOrNo += 1;
			}
		}

		if (yesOrNo) {
			cout << "no\n";
		}
		else {
			cout << "yes\n";
		}
	}

	return 0;
}

//다른 사람이 푼 문제
// reverse함수를 사용하여 문제를 해결하였다.
#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef pair<lint, lint> pi;
const int mod = 1e9 + 7;

int main() {
	while (1) {
		string s;
		cin >> s;
		if (s == "0") break;
		string t = s;
		reverse(t.begin(), t.end());
		puts(t == s ? "yes" : "no");
	}
}