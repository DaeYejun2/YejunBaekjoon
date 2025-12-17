import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007

base_matrix = [[1, 1], [1, 0]]

def mul(A, B):
    C = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[j][k]) % p
    return C
    
def power(A, n):
    if n == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A
    
    tmp = power(A, n//2)
    if n%2:
        return mul(mul(tmp, tmp), A)    #A는 base_matrix죠
    else:
        return mul(tmp, tmp)


A = power(base_matrix, n)
print(A[0][1])