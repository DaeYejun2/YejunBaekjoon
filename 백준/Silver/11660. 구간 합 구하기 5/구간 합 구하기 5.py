import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0] for _ in range(n)]

for i in range(n):
    for j in range(n):
        prefix_sum[i].append(prefix_sum[i][j] + data[i][j])

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    tmp = 0
    for j in range(x2-x1+1):
        tmp += prefix_sum[x1+j-1][y2] - prefix_sum[x1+j-1][y1-1]
    print(tmp)