import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().rstrip().split())
INF = int(1e8)

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

import heapq
q = []
distance[x] = 0
heapq.heappush(q,(0,x))

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue

    for next_node, d in graph[now]:
        tmp = distance[now]+d
        if tmp < distance[next_node]:
            distance[next_node] = tmp
            heapq.heappush(q, (tmp, next_node))

res = []
for i, d in enumerate(distance[1:]):
    if d == k:
        res.append(i+1)

if not res: print(-1)
else:
    print('\n'.join(map(str,res)))