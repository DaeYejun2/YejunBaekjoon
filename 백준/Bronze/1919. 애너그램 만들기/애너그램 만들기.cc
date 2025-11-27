#include<bits/stdc++.h>
using namespace std;

int main() {

	int arr[26] = {};
	int ans = 0;
	string a, b;
	
	cin >> a ;
	cin >> b;
	
	for (auto i : a) arr[i - 'a']++;
	for (auto i : b) arr[i - 'a']--;
	for (auto i : arr) ans += abs(i);
	cout << ans;
}