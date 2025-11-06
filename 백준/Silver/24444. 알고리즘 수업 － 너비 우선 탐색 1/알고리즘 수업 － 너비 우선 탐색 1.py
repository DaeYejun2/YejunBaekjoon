from collections import deque
import sys
input = sys.stdin.readline
#인접행렬
cnt = 0
n, m, v= map(int, input().split())
visited = [0] * (n+1)
matrix = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in range(1, n+1):     #각 정점별로 연결된 정점들 오름차순으로 정렬
    matrix[i].sort()
    
def bfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt
    queue = deque()
    queue.append(v)
    
    while queue:
        v = queue.popleft()
        for i in matrix[v]:
            if visited[i] == 0:
                cnt+=1
                queue.append(i)
                visited[i] = cnt
                
bfs(v)

for i in range(1, n+1):
    print(visited[i], end='\n')