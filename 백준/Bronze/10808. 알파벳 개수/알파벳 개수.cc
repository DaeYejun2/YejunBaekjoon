#include<bits/stdc++.h>
using namespace std;

int main(void) {
	vector<int> data(26, 0);
	
	string s;
	cin >> s;

	for (int i = 0; i < s.size(); i++) {
		int d = int(s[i]) - 97;
		data[d]++;
	}

	for (int e : data) {
		cout << e << ' ';
	}
}