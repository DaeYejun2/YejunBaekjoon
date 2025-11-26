import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<r and 0<=ny<c and 0<=nz<l and not visited[nz][nx][ny]:   #범위에서 벗어나지 않았다면
                if data[nz][nx][ny] == '.' or data[nz][nx][ny] == 'E' :  #가려는데가 .이고, 방문하지 않았다면
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append((nz,nx,ny))
                if data[nz][nx][ny] == 'E':
                    print(f'Escaped in {visited[nz][nx][ny] - 1} minute(s).')
                    return
    print("Trapped!")
        
while True:
    q = deque()
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0: break
    data = []
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        data.append([list(input().rstrip()) for _ in range(r)])
        tmp = input()

    for k in range(l):
        for i in range(r):
            for j in range(c):
                if data[k][i][j] == 'S':
                    q.append((k, i, j))
                    visited[k][i][j] = 1
                    break
     
    bfs()