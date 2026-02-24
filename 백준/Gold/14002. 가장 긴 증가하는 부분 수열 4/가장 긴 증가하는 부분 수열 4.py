import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

dp = [1]*n
res = [data[0]]
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

m = max(dp)
print(m)
res = []
for i in range(n-1,-1,-1):
    if dp[i] == m:
        res.append(data[i])
        m -= 1

print(*res[::-1])