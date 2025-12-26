import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [1] * n

for j in range(1, n):
    chk = 0
    big = 0
    for i in range(j, 0, -1):
        if data[j] > data[i-1]:
            if dp[j] < dp[i-1]+1:
                dp[j] = dp[i-1]+1
        elif data[j] == data[i-1]:
            if dp[j] < dp[i-1]:
                dp[j] = dp[i-1]

print(max(dp))