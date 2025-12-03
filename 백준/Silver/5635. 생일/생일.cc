#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<pair<pair<int, int>, pair<int, string>>> v(n);	//년, 월, 일, 이름 순.
	
	for (int i = 0; i < n; i++) {
		cin >> v[i].second.second >> v[i].second.first >> v[i].first.second >> v[i].first.first;   //입력 받는건 알아서 조정 잘 하시고
	}
	sort(v.begin(), v.end());	//기본적으로 오름차순 정렬

	cout << v[n - 1].second.second << '\n' << v[0].second.second;
}