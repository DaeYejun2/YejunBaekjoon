n = int(input())
m = int(input())
INF = int(1e8)

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
pre = [0] * (n+1)

for i in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

s, e = map(int, input().split())

import heapq

q = []
heapq.heappush(q, (0, s))
distance[s] = 0

while q:
    dist, now = heapq.heappop(q)
        
    if distance[now] < dist:
        continue

    for next_node, cost in graph[now]:
        if dist+cost < distance[next_node]:
            distance[next_node] = dist+cost
            heapq.heappush(q, (dist+cost, next_node))
            pre[next_node] = now

print(distance[e])
path = []
curr = e
while curr != 0:
    path.append(curr)
    curr = pre[curr]

path.reverse()

print(len(path))
print(*path)