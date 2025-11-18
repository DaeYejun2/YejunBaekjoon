import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n)]
dp[0] = [0,1,1,1,1,1,1,1,1,1]       #dp[자리수][끝자리 수]

for i in range(1,n):
    dp[i][0] = dp[i-1][1]           #끝자리가 0이면, 그 다음 자리는 1밖에 못옴 1,0 = 0,1. 앞 자릿수에서 1인 경우 받아오기.
    dp[i][9] = dp[i-1][8]           #끝자리가 9면, 그 다음 자리는 8밖에 못옴  앞 자릿수에서 8인 경우 받아오기.
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]  #0, 9 둘다 아니면, 위 아래 수 다 가능. 
        
print(sum(dp[n-1])%1000000000)