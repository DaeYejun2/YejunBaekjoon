import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(current_x, current_y, x, y, n):
    if current_x == x and current_y == y: return 0
    q = deque()
    q.append((current_x, current_y))
    while q:
        current_x, current_y = q.popleft()
        for i in range(8):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not data[nx][ny]:
                    data[nx][ny] = data[current_x][current_y] + 1
                    q.append((nx, ny))
                elif data[current_x][current_y] + 1 < data[nx][ny]:
                    data[nx][ny] =  data[current_x][current_y] + 1
                    q.append((nx, ny))
                if nx == x and ny == y: return data[nx][ny]

for i in range(t):
    n = int(input())
    data = [[0] * n for _ in range(n)]
    current_x, current_y = map(int, input().split())
    x, y = map(int, input().split())
    print(bfs(current_x, current_y, x, y, n))