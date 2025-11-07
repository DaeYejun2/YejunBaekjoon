import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
m, n = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1의 위치 찾아서 큐에 넣어 놓기
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1: queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

bfs()
max_t = 0
has_zero = any(0 in row for row in matrix)
if has_zero:
    print(-1)
else:
    for i in range(n):
        for j in range(m):
            if max_t < matrix[i][j]: max_t = matrix[i][j]
    print(max_t - 1)