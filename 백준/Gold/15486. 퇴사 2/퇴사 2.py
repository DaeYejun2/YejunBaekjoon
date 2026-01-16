import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti); p.append(pi)

dp = [0]*(n+1)

for i in range(n-1, -1, -1):
    if i + t[i] <= n:
        dp[i] = max(dp[i+1], dp[i+t[i]]+p[i])
    else:
        dp[i] = dp[i+1]
        
print(dp[0])