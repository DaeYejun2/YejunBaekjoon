import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

t = int(input())
def dfs(x, y):
        #범위를 벗어나는 경우 종료
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        #방문한 적이 없다면. 즉, 초기 상태인 1이라면
        if matrix[x][y] == 1:
            matrix[x][y] = 2
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False

for i in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*n for _ in range(m)]

    for i in range(k):
        a, b = map(int, input().split())
        matrix[a][b] = 1

    result = 0

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
                
    print(result)