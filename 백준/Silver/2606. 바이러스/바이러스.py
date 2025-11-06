import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [0] * (n+1)
matrix = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
for i in range(1, n+1):
    matrix[i].sort()

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    
    while queue:
        v = queue.popleft()
        for i in matrix[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

bfs(1)
cnt = 0
for i in range(2, n+1):
    if visited[i] != 0:
        cnt+=1
        
print(cnt)