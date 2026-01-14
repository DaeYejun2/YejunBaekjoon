import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
index = [0]*(n+1)

if n >= 2:
    dp[2] = 1
    index[2] = 1
    
for i in range(3, n+1):
    dp[i] = dp[i-1] + 1
    index[i] = i-1
    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3]+1
        index[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2]+1
        index[i] = i//2
print(dp[n])
i = n
while i != 0:
    print(i, end=' ')
    i = index[i]