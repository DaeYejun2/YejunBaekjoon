import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    d = [1, 1, 1, 2, 2]
    n = int(input())
    for i in range(5, n):
        d.append(d[i-1]+d[i-5])
    print(d[n-1])