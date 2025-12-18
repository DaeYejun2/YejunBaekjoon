import sys
input = sys.stdin.readline
#중복 순열 문제. n^m
n, m = map(int, input().split())
data = []

def backtraking():
    if len(data) == m:
        print(' '.join(map(str, data)))
        return
    for i in range(1, n+1):
            data.append(i)
            backtraking()
            data.pop()
    
backtraking()