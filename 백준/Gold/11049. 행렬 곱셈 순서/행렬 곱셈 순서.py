import sys
input = sys.stdin.readline

n = int(input())
p = [tuple(map(int,input().split())) for i in range(n)]

dp = [[0] * n for _ in range(n)]

for dist in range(n-1): # 시작점 i와 끝점 j 사이의 거리
    for i in range(n-1-dist): # 시작점 i가 어디까지 갈수 있는가. j는 마지막 인덱스인 n-1보다 작거나 같아야 함
        j = i+dist+1 # 구간의 길이는 고정, i만 옆으로 한칸씩 밀며 dist+1은 유지하며 이동.
        dp[i][j] = float('inf')
        for k in range(i,j):
            cost = dp[i][k]+dp[k+1][j] + p[i][0]*p[k][1]*p[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][-1])