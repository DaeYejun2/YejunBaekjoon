import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().rstrip())))
    
def rec(x, y, n):
    d = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if d != data[i][j]:
                print("(",end='')
                m = n // 2
                rec(x, y, m)
                rec(x, y+m, m)
                rec(x+m, y, m)
                rec(x+m, y+m, m)
                print(")",end='')
                return
    if d == 1: print(1,end='')
    else:print(0,end='')
    

rec(0, 0, n)