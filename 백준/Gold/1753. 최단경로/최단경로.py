import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

import heapq

q = []
distance[start] = 0
heapq.heappush(q,(0,start))

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist: continue

    for next_node, cost in graph[now]:
        if distance[next_node] > dist+cost:
            distance[next_node] = dist+cost
            heapq.heappush(q, (dist+cost, next_node))

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])