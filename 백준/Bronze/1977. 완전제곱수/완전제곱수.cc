#include<iostream>
using namespace std;

int main() {
	int m, n;
	int _sum = 0, _min = 10001;

	cin >> m;
	cin >> n;

	for (int i = 1; i <= 100; i++)
		if (i * i >= m && i * i <= n) {
			if (_min > i * i) _min = i * i;
			_sum += i * i;
		}
	if (_min == 10001) cout << -1;
	else cout << _sum << '\n' << _min;

}