import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e8)
distance = [INF] * 100001
#tmp = 0
min_val = INF
pre = [0] * 100001

q = deque()
distance[n] = 0
q.append((n, 0))

while q:
    curr, cost = q.popleft()

    for i in [curr-1, curr+1, 2*curr]:
        if 0 <= i <= 100000 and distance[i] > cost + 1:
            pre[i] = curr
            distance[i] = cost+1
            q.append((i, cost+1))

print(distance[k])

res = []
curr = k
for i in range(distance[k]+1):
    res.append(curr)
    curr = pre[curr]

print(*res[::-1])
