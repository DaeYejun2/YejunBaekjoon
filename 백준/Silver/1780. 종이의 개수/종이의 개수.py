import sys
input = sys.stdin.readline

result = [0, 0, 0]  #-1, 0, 1 순서
paper = []
n = int(input())

for i in range(n):
    paper.append(list(map(int, input().split())))
    
def rec(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                m = n // 3
                rec(x, y, m)
                rec(x, y+m, m)
                rec(x, y+2*m, m)
                rec(x+m, y, m)
                rec(x+m, y+m, m)
                rec(x+m, y+2*m, m)
                rec(x+2*m, y, m)
                rec(x+2*m, y+m, m)
                rec(x+2*m, y+2*m, m)
                return 
    if color == -1: result[0] += 1
    elif color == 0: result[1] += 1
    else: result[2] += 1

rec(0, 0, n)

for i in range(3):
    print(result[i])