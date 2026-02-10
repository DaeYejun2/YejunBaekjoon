dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

def solution(n):
    res = [[0] * n for _ in range(n)]
    x, y = 0, 0
    res[x][y] = 1
    i = 2
    idx = 0
    
    while i <= n * n: # n*n까지 포함되어야 함
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        # [핵심 수정] 벽 안쪽이고 + 동시에 아직 안 가본 칸(0)일 때만 전진!
        if 0 <= nx < n and 0 <= ny < n and res[nx][ny] == 0:
            res[nx][ny] = i
            x, y = nx, ny # 현재 위치 갱신
            i += 1
        else:
            # 벽에 부딪히거나 이미 가본 칸이면 방향만 바꿈
            idx = (idx + 1) % 4
            
    return res
