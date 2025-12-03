import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
#u, v를 먼저 저장하고 방문표시하면 되는거 아닌가
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
u, v = map(int, input().split())

def dijkstra(start, end):
    distance = [INF]*(n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: 
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance[end]

#u, v를 무조건 지나야하므로, 1에서 u까지, u에서 v까지 우선적으로 거리를 구해 놓을 다음에, v에서 n까지 간다
#무방향 그래프이므로 u->v, v->u 두가지 경우 모두 탐색

route1 = dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, n)
route2 = dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, n)

if route1 >= INF and route2 >= INF: print(-1)
else: print(min(route1, route2))