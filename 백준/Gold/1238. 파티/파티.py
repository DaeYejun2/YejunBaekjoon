n, m, x = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

import heapq

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: continue

        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    return distance[end]

res = []
for i in range(1, n+1):
    go = dijkstra(i, x)
    back = dijkstra(x, i)
    res.append(go+back)

print(max(res))