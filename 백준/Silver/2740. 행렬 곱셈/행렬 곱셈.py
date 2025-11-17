import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(m)]
result = [[] for _ in range(n)]

for i in range(n):
    for l in range(k):
        sum = 0
        for j in range(m):
            sum = sum + (matrix1[i][j] * matrix2[j][l])
        result[i].append(sum)

for i in range(n):
    print(*result[i])