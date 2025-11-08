import sys
input = sys.stdin.readline

n = int(input())
m = n
paper = []
result =[0,0]

for i in range(n):
    paper.append(list(map(int,input().rstrip().split())))

def rec(y, x, n):
    color = paper[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            # 안에 있는 색이 완전히 같지 않다면 if문 실행
            if color != paper[i][j]:
                m = n // 2
                rec(y, x, m)
                rec(y, x+m, m)
                rec(y+m, x, m)
                rec(y+m, x+m, m)
                return
    if color == 1: result[0] += 1
    else: result[1] += 1
    
rec(0, 0, n)

print(result[1],'\n',result[0],sep='')