import sys
import heapq
input = sys.stdin.readline

n = int(input())
sec = [[300], [60], [10]]
for i in range(3): sec[i].append(0)

for i in range(3):
    sec[i][1] = n // sec[i][0]
    n %= sec[i][0]
if n != 0: print(-1)
else:
    for i in range(3): print(sec[i][1], end=' ')