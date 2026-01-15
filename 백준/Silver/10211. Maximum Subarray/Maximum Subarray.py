import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = data[0]
    for j in range(1, n):
        dp[j] = max(data[j], dp[j-1]+data[j])
    print(max(dp))