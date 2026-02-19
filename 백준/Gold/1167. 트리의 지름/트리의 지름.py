import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v = int(input())
graph = [[] for _ in range(v+1)]

for i in range(1,v+1):
    data = list(map(int,input().split()))
    for d in range(1, len(data)-1,2):
        graph[data[0]].append((data[d], data[d+1]))
        graph[data[d]].append((data[0], data[d+1]))

def dfs(v, distance):
    for next_node, weight in graph[v]:
        if dist[next_node] == -1:
            dist[next_node] = distance+weight
            dfs(next_node, distance+weight)

dist = [-1]*(v+1)
dist[1] = 0
dfs(1,0)
start_node = dist.index(max(dist))

dist = [-1]*(v+1)
dist[start_node] = 0
dfs(start_node,0)
print(max(dist))