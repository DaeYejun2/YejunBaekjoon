import sys
input = sys.stdin.readline

chess = [[0]*6 for _ in range(6)]   #방문 dragon
chk = 0
dx = [-1, 1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]


for i in range(36):
    tmp = 0
    c = input().strip()
    x = ord(c[0])-65
    y = int(c[1])-1
    if i == 0:
        fx = x; fy = y    #첫번째 값
        rx = x; ry = y    #이전 값
        chess[x][y] += 1
    else:
        for j in range(8):
            nx = rx+dx[j]
            ny = ry+dy[j]
            
            if nx == x and ny == y:
                tmp = 1
                chess[x][y] += 1
                rx = nx; ry = ny
                break
                
        if tmp == 0 or chess[x][y] > 1:
            chk = 1  

if chk == 1: 
    print("Invalid")
    exit()
else:
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx == fx and ny == fy:
            print("Valid")
            exit()
print("Invalid")