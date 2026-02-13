dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board, h, w):
    le = len(board)
    res = 0
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < le and 0 <= ny < le:
            if board[nx][ny] == board[h][w]:
                res += 1
    return res