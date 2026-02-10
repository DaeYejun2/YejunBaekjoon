dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def solution(board):
    n = len(board)
    bomb = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb[i][j] = 1
                x = i; y = j
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        bomb[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            if bomb[i][j] == 0: cnt += 1

    return cnt