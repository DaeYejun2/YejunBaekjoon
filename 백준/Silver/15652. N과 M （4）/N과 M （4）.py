import sys
input = sys.stdin.readline
# 조합 문제
n, m = map(int, input().split())
data = []

def backtraking(start):
    if len(data) == m:
        print(' '.join(map(str, data)))
        return
    for i in range(start, n+1):
        data.append(i)
        backtraking(i)
        data.pop()

backtraking(1)