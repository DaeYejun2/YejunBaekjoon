import sys
input = sys.stdin.readline

t = int(input())
#출력: 0출력 1출력
zero = [0]*41
one = [0]*41
zero[0], one[0] = 1, 0
zero[1], one[1] = 0, 1

for i in range(t):
    n = int(input())
    for i in range(2, n+1):
        zero[i] = zero[i-2]+zero[i-1]
        one[i] = one[i-2]+one[i-1]
    print(zero[n], one[n])