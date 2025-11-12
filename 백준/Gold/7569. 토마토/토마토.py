import sys
from collections import deque
input = sys.stdin.readline

n, m, h = map(int, input().split())
tomato = [[] for _ in range(h)]
queue = deque()

for j in range(h):
    for i in range(m):
        tomato[j].append(list(map(int, input().split())))

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [1, -1, 0, 0, 0, 0]

for k in range(h):
    for i in range(m):
        for j in range(n):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j))

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue

            if tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append((nz, nx, ny))

bfs()
max_t = 0
has_zero = any(0 in r for p in tomato for r in p)
if has_zero:
    print(-1)
else:
    for k in range(h):
        for i in range(m):
            for j in range(n):
                if max_t < tomato[k][i][j]: max_t = tomato[k][i][j]
    print(max_t - 1)