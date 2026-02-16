n = int(input())
m = int(input())
INF = int(1e8)

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]


for i in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

s, e = map(int, input().split())
pre = [[s] for _ in range(n+1)] # 역추적 테이블

import heapq

q = []
heapq.heappush(q, (0, s))
distance[s] = 0

while q:
    dist, now = heapq.heappop(q)
        
    if distance[now] < dist:
        continue

    for next_loc, cost in graph[now]:
        if dist+cost < distance[next_loc]:
            distance[next_loc] = dist+cost
            heapq.heappush(q, (dist+cost, next_loc))
            pre[next_loc] = pre[now] + [next_loc]

print(distance[e])
print(len(pre[e]))
print(*pre[e])