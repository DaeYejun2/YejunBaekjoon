import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

tetrominoes = [
    # ㅡ 모양
    [(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)],
    # ㅁ 모양
    [(0,0), (0,1), (1,0), (1,1)],
    # L 모양
    [(0,0), (1,0), (2,0), (2,1)], [(0,0), (1,0), (2,0), (2,-1)],
    [(0,0), (0,1), (0,2), (1,0)], [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (0,1), (1,1), (2,1)], [(0,0), (1,0), (2,0), (0,1)],
    [(0,0), (1,0), (1,1), (1,2)], [(0,0), (0,1), (0,2), (-1,2)],
    # S 모양
    [(0,0), (1,0), (1,1), (2,1)], [(0,0), (1,0), (1,-1), (2,-1)],
    [(0,0), (0,1), (-1,1), (-1,2)], [(0,0), (0,1), (1,1), (1,2)],
    # ㅗ 모양
    [(0,0), (0,1), (0,2), (1,1)], [(0,0), (0,1), (0,2), (-1,1)],
    [(0,0), (1,0), (2,0), (1,1)], [(0,0), (1,0), (2,0), (1,-1)]
]

max_val = 0

for i in range(n):
    for j in range(m):
        for shape in tetrominoes:
            current_sum = 0
            is_possible = True
            
            for dr, dc in shape:
                nr, nc = i + dr, j + dc
                # 범위를 벗어나면 즉시 중단
                if 0 <= nr < n and 0 <= nc < m:
                    current_sum += board[nr][nc]
                else:
                    is_possible = False
                    break

            if is_possible:
                if current_sum > max_val:
                    max_val = current_sum

print(max_val)