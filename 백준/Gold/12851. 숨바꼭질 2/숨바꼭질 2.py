import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e8)
distance = [INF] * 100001
tmp = 0
min_val = INF

q = deque()
distance[n] = 0
q.append((n, 0))

while q:
    curr, cost = q.popleft()

    for i in [curr-1, curr+1, 2*curr]:
        if 0 <= i <= 100000 and distance[i] >= cost + 1:
            if i == k:
                if min_val == cost+1: tmp += 1
                else:
                    min_val = min(distance[k], cost+1)
                    tmp = 0
            
            distance[i] = cost+1
            q.append((i, cost+1))

print(distance[k])
print(tmp+1)