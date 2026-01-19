import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for _ in range(n): data.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= data[i-1][0]:  #현재 최대 무게(j)가 해당 물건 무게 보다 큰 경우
            #표의 윗 셀의 값과/ 현재 물건 v+이전 물건의 v의 최대값을 dp[i][j]에 저장
            dp[i][j] = max(data[i-1][1]+dp[i-1][j-data[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[n][k])