import sys
input = sys.stdin.readline

def dp(n):
    if n >= 1:
        d[1] = 1
    if n >= 2:
        d[2] = 1
    if n >= 3:
        d[3] = 1
    if n >= 4:
        d[4] = 2
    if n >= 5:
        d[5] = 2
    for i in range(5, n+1):
        d[i] = d[i-1] + d[i-5]
    return d[n]

t = int(input())
for i in range(t):
    n = int(input())
    d = [0] * (n+1)
    print(dp(n))