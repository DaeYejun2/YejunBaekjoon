import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
cctv = []
direction = [   # 0:왼, 1:위, 2:오, 3: 아래
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for i in range(n):
    row = list(map(int, input().split()))
    data.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctv.append((row[j], i, j))  #cctv 종류와 갯수
            
min_val = int(1e9)

def watch(x, y, dir, tmp):
    for d in dir:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: break
            if tmp[nx][ny] == 6: break
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = '#'

def dfs(depth, data):
    global min_val
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += data[i].count(0)
        min_val = min(cnt, min_val)
        return
    
    tmp = copy.deepcopy(data)
    cctv_num, x, y = cctv[depth]
    for dir in direction[cctv_num]:
        watch(x, y, dir, tmp)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(data)
        
dfs(0, data)
print(min_val)