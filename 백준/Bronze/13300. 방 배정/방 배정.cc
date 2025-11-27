#include<bits/stdc++.h>
using namespace std;

//1학년에서 6학년까지 방 배정
//남학생은 남학생끼리만, 여학생은 여학생끼리만, 
//한 방에는 같은 학년
//한방에 한명만 배정하는 것도 가능
//조건에 맞게 필요한 최소 방의 수
//여학생은 0, 남학생은 1. S

int student[2][7];
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, k;
	int s, y;
	int cnt = 0;
	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		cin >> s >> y;    //s는 성별, y는 학년
		student[s][y]++;
	}

	for (int i = 0; i < 2; i++) {
		for (int j = 1; j < 7; j++) {
			cnt += student[i][j] / k;
			if (student[i][j] % k) ++cnt;
		}
	}
	cout << cnt;
}