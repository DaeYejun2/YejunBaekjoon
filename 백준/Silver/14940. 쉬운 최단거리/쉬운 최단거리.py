import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
visited = [[-1] * m for _ in range(n)]
queue = deque()
for i in range(n):
    maze.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            visited[i][j] = 0
            queue.append((i, j))
        elif maze[i][j] == 0:
            visited[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]+1; #방문표시
                    queue.append((nx, ny))
            
bfs()

for i in range(n):
    print(*visited[i])