from collections import deque

def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    x,y=0,0
    visited[0][0] = True
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 0:
                if not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    if maps[n-1][m-1] == 1: return -1
    else: return maps[n-1][m-1]