import sys
input = sys.stdin.readline

n = int(input())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]
#result = [[] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        sum = 0
        for k in range(n):
            sum = sum | (matrix1[i][k] & matrix2[k][j])
        # result[i].append(sum)
        if sum == 1: cnt += 1

print(cnt)