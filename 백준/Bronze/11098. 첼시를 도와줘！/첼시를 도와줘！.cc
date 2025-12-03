#include<iostream>
using namespace std;

int main() {
	int n, p;
	cin >> n;
	while (n--) {
		int _max = 0, price;
		cin >> p;
		string s, ans;
		while (p--) {
			cin >> price >> s;
			if (_max < price) {
				_max = price;
				ans = s;
			}
		}
		cout << ans << '\n';
	}

}