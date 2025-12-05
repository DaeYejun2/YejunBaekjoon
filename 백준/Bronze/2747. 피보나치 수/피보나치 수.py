import sys
input = sys.stdin.readline

dp = [0] * 51
dp[1] = 1
n = int(input())

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]
    
print(dp[n])