import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().rstrip())))
    
apt = []
cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if matrix[x][y] == 1:
        cnt+=1
        matrix[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            apt.append(cnt)
            cnt = 0

apt.sort()
print(len(apt))
print('\n'.join(map(str,apt)))