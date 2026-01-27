import sys
input = sys.stdin.readline

t = int(input())
data = []
for _ in range(t):
    data.append(int(input()))
m = max(data)

arr = [True] * (m+1)
arr[0] = arr[1] = False
prime = []
for i in range(2, m+1):
    if arr[i]:
        prime.append(i)
        for j in range(i*i, m+1, i):
            arr[j] = False

for d in data:
    for p in prime:
        if p > d//2: break
        if arr[d-p]:
            tmp = (p, d-p)
    print(*tmp)