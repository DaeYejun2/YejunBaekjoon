import sys
input = sys.stdin.readline

#세로 N, 가로 M, 작업을 시작할 때 인벤토리에는 B개의 블록
# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.  -> 2초  del_block
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다  -> 1초  put_block
# 땅고르는데 최소 시간. 만약 답이 여러개면? 땅의 높이가 가장 높은 애 출력

n, m, b = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]
result = int(1e9)
lev = 0

for i in range(257):    #땅의 높이가 257이니 1층부터 위로
    #i층. 즉, 0층이 되기 위한 블록의 양과 시간을 구하면 되겠네요
    del_block, put_block = 0, 0
    for x in range(n):
        for y in range(m):
            if data[x][y] >= i:    #블록이 i(층)보다 크거나 같다면, 크니까 블럭을 빼야겠죠?
                del_block += data[x][y] - i
            else:
                put_block += i - data[x][y]
                
    if put_block > b + del_block:  # 인벤토리 블럭보다 뺀 블럭이 더 많을 때
        continue
    cnt = del_block*2 + put_block
    if result >= cnt:
        result = cnt
        lev = i
        
print(result, lev)