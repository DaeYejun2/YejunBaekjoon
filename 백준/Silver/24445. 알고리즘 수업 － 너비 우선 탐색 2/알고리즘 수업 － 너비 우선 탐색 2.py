import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
visited = [0] * (n+1)
matrix = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
for i in range(1, n+1):
    matrix[i].sort(reverse=True)

order = 1

def bfs(v):
    global order
    visited[v] = order
    queue = deque()
    queue.append(v)
    
    while queue:
        v = queue.popleft()
        for i in matrix[v]:
            if visited[i] == 0:
                order += 1
                visited[i] = order
                queue.append(i)

bfs(v)

for i in range(1, n+1):
    print(visited[i], end='\n')