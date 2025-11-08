import sys
input = sys.stdin.readline

n = int(input())
tree = []
for i in range(n):
    tree.append(list(map(int, input().rstrip())))
    
def Quad_tree(y, x, n):
    chk = tree[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if chk != tree[i][j]:
                m = n // 2
                print('(',end='')
                Quad_tree(y, x, m)
                Quad_tree(y, x+m, m)
                Quad_tree(y+m, x, m)
                Quad_tree(y+m, x+m, m)
                print(')',end='')
                return
    if chk == 1: print('1',end='')
    else: print('0',end='')
    
Quad_tree(0,0,n)