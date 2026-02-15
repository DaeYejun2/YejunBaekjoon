n=int(input())
target=int(input())

end_num = n*n
i = 2
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
turn = 0
# 두번 지나면 방향을 바꾼다
arr = [[0]*n for _ in range(n)]
x, y=n//2, n//2
arr[x][y] = 1
ans_x, ans_y = 0,0
if target == 1: 
    ans_x = x
    ans_y = y
tmp = 2
cnt = 1
while i <= end_num:
    for _ in range(tmp): # 방향 바꾸기 2 고정
        dx, dy = dirs[turn]
        for j in range(cnt):
            nx,ny = x+dx, y+dy
            if arr[nx][ny] == 0:
                arr[nx][ny] = i
                if i == target and target != 1: ans_x, ans_y = nx,ny
                x,y=nx,ny
                i += 1
        turn = (turn+1)%4
    cnt += 1

# 방향 바꾸는걸 2번 - for문
# 위의 for문을 몇번 갈건지도 정해야 됨
    
for a in arr:
    print(*a)
print(ans_x+1, ans_y+1)