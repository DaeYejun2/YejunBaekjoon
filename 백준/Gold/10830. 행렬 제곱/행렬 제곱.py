import sys
input = sys.stdin.readline
m = 1000
def mul(n, matrix1, matrix2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
            res[i][j] %= m
    return res

def power(n, b, matrix):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    
    tmp = power(n, b//2, matrix)
    if b % 2 == 0: return mul(n, tmp, tmp)
    else: return mul(n, mul(n, tmp, tmp), matrix)

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
for row in power(n,b,matrix):
    print(*(row))