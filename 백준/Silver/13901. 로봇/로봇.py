import sys
input = sys.stdin.readline

r, c = map(int, input().split())
# 방문 여부와 장애물을 한 번에 관리 (0: 빈칸, 1: 장애물/방문함)
grid = [[0] * c for _ in range(r)]

k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    grid[br][bc] = 1 # 장애물 표시

sr, sc = map(int, input().split())
# 이동 방향 순서 (1:상, 2:하, 3:좌, 4:우)
directions = list(map(int, input().split()))

# dx, dy 인덱스를 문제의 1,2,3,4와 맞춤 (0번 인덱스는 버림)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

curr_r, curr_c = sr, sc
grid[curr_r][curr_c] = 1 # 시작 위치 방문 처리
dir_idx = 0 # directions 리스트의 인덱스

while True:
    moved = False
    # 최대 4번 방향을 돌려보며 갈 곳을 찾음
    for _ in range(4):
        d = directions[dir_idx]
        nr, nc = curr_r + dr[d], curr_c + dc[d]

        # 갈 수 있는 경우 (범위 내 + 장애물X + 방문X)
        if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 0:
            # 해당 방향으로 끝까지 직진
            while 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 0:
                grid[nr][nc] = 1 # 방문 처리
                curr_r, curr_c = nr, nc
                nr, nc = curr_r + dr[d], curr_c + dc[d]
                moved = True
            # 한 번이라도 움직였다면 방향 순서는 유지한 채 다시 체크
            break 
        else:
            # 막혔다면 다음 방향으로 이동
            dir_idx = (dir_idx + 1) % 4
    
    # 4방향 모두 시도했는데 한 번도 못 움직였다면 종료
    if not moved:
        break

print(curr_r, curr_c)