# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. -> 2초
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. -> 1초
import sys
input = sys.stdin.readline

n, m, b = map(int,input().split())
minecraft = []

for i in range(n):
    minecraft.append(list(map(int, input().split())))

ans = int(1e9)
glevel = 0

for i in range(257): # 땅의 높이 256까지 i 가 1이면 1층인경우 마크땅 전체가 1과 비교
    use_block = 0
    take_block = 0
    for x in range(n):
        for y in range(m):
            if minecraft[x][y] > i:   # 마크 땅이 i보다 더 높으면 블럭 회수 2초
                take_block += minecraft[x][y] - i
            else:              # 마크 땅이 i보다 낮으면 블럭 추가 1초
                use_block += i - minecraft[x][y]
# 이해를 위한 2가지 case
# 전체가 0, 하나만 1, i=0인 경우 생각
# 전체가 1, 하나만 0, i = 1인 경우 생각
    if use_block > b + take_block:
        continue
    
    cnt = take_block * 2 + use_block
    
    if ans >= cnt:
        ans = cnt
        glevel = i
        
print(ans, glevel)