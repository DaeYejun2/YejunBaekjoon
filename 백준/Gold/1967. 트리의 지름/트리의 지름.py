import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, weight = map(int,input().split())
    graph[p].append((c, weight))
    graph[c].append((p, weight))

def dfs(v, distance):
    for next_node, weight in graph[v]:
        if dist[next_node] == -1:
            dist[next_node] = distance+weight
            dfs(next_node, distance+weight)

dist = [-1]*(n+1)
dist[1] = 0
dfs(1,0)
start_node = dist.index(max(dist)) # 찾은 노드 중 가장 먼(긴) 노드 번호 확인

# 가장 긴 노드에서 다른 노드까지 거리 확인
dist = [-1]*(n+1)
dist[start_node] = 0
dfs(start_node, 0)

print(max(dist))