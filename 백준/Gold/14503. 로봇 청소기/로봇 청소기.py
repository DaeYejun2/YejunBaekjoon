import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# 방향: 0북, 1동, 2남, 3서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1
    
    clean_exits = False
        
    for _ in range(4):
        d = (d+3)% 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            r, c = nx, ny
            clean_exits = True
            break
    
    if not clean_exits:
        bx = r - dx[d]
        by = c - dy[d]
        if 0 <= bx < n and 0 <= by < m and board[bx][by] != 1:
            r, c = bx, by
        else:
            break
        
print(cnt)