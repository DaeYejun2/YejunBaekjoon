import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [input().rstrip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            x, y = i, j
            visited[x][y] = True
            break
        
def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                if maps[nx][ny] == 'P':
                    cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    if cnt == 0: print('TT')
    else: print(cnt)

bfs(x, y)