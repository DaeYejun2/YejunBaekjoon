c, r = map(int, input().split())
k = int(input())

arr = [[0]*c for _ in range(r)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
turn = 0
i = 2
x,y = r-1,0
arr[x][y] = 1
ax, ay = -1, -1
if k == 1: ax,ay=1,1

while i <= c*r:
    dx,dy = dirs[turn]
    nx,ny = x+dx, y+dy
    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 0:
        arr[nx][ny] = i
        if i == k:
            ax, ay = r - nx,ny+1
        i += 1
        x,y=nx,ny
    
    else:
        turn = (turn+1)%4

if ax == -1: print(0)
else: print(ay, ax)