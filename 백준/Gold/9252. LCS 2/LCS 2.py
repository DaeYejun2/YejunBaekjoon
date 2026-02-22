import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
n = len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])

res = []
i,j = n,m

while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
        res.append(str1[i-1])
        i-=1
        j-=1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1

print(''.join(res[::-1]))