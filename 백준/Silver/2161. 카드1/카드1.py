import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = [i for i in range(1, n+1)]
res = []
arr = deque(arr)

while len(arr) != 1:
    res.append(arr.popleft())
    arr.append(arr.popleft())

print(*res, arr[0])