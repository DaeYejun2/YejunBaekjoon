import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(w, h):
    while q_f:
        x, y = q_f.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] != '#' and not visited_f[nx][ny]:
                    q_f.append((nx, ny))
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    
    while q_s:
        x, y = q_s.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] != '#' and not visited_s[nx][ny]:
                    if visited_s[x][y] + 1 < visited_f[nx][ny] or not visited_f[nx][ny]:
                        q_s.append((nx, ny))
                        visited_s[nx][ny] = visited_s[x][y] + 1
            else:
                return (visited_s[x][y])
    return "IMPOSSIBLE"
                    
for i in range(t):
    q_s = deque()
    q_f = deque()
    w, h = map(int, input().split())
    visited_s = [[0] * w for _ in range(h)]
    visited_f = [[0] * w for _ in range(h)]
    data = [list(input().rstrip()) for _ in range(h)]
    for a in range(h):
        for b in range(w):
            if data[a][b] == '@': 
                q_s.append((a, b))
                visited_s[a][b] = 1
            elif data[a][b] == '*': 
                q_f.append((a, b))
                visited_f[a][b] = 1
    print(bfs(w, h))