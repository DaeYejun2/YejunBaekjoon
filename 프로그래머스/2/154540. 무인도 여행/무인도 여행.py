from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = []

def bfs(i, j, x, y, maps, visited):
    queue = deque()
    queue.append((i, j))
    tmp = int(maps[i][j])
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < x and 0 <= ny < y and maps[nx][ny]!='X':
                if visited[nx][ny] == 0:
                    tmp += int(maps[nx][ny])
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    return tmp

def solution(maps):
    x = len(maps)
    y = len(maps[0])
    visited = [[0]*y for i in range(x)]
    cnt = 0
    for i in range(x):
        for j in range(y):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                visited[i][j] = 1
                res.append(bfs(i, j, x, y, maps, visited))
    res.sort()
    if len(res) == 0: return [-1]
    return res