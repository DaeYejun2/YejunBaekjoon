import sys
import heapq
input = sys.stdin.readline
INF=int(1e9)

n, k = map(int,input().split())


distance = [INF]*100001
distance[n] = 0
q = []
heapq.heappush(q,(0, n))

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue

    if now*2 <= 100000 and distance[now*2] > dist:
        distance[now*2] = dist
        heapq.heappush(q, (dist, now*2))

    for next_node in [now-1, now+1]:
        if 0 <= next_node <= 100000 and distance[next_node] > dist + 1:
            distance[next_node] = dist+1
            heapq.heappush(q,(dist+1, next_node))

print(distance[k])