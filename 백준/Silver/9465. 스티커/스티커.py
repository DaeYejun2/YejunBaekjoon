import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    data=[]
    n = int(input())
    for _ in range(2):
        data.append(list(map(int,input().split())))
    dp = [[0]*n for _ in range(2)]

    # 스티커 길이가 1
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]
    if n == 1:
        print(max(dp[0][0],dp[1][0]))
        continue

    # 스티커 길이가 2
    dp[0][1] = data[1][0]+data[0][1]
    dp[1][1] = data[0][0]+data[1][1]
    if n == 2:
        print(max(dp[0][1],dp[1][1]))
        continue

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + data[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + data[1][i]

    print(max(dp[0][-1], dp[1][-1]))