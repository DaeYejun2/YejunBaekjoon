import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for i in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs():
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = v

bfs()
print('\n'.join(map(str, visited[2:])))