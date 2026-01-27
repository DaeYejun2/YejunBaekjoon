import sys
input = sys.stdin.readline

t = int(input())
data = []
for _ in range(t):
    data.append(int(input()))
m = max(data)
arr = [i for i in range(m+1)]; arr[1] = 0
end = int(m**0.5)
prime = []

for i in range(2, m+1):
    if arr[i]:
        prime.append(i)
    for j in range(i*i, m+1, i):
        arr[j] = 0

for d in data:
    res = [0]*(m+1)
    tmp = d
    for p in prime:
        if p > tmp: break
        while tmp % p == 0:
            tmp //= p
            res[p] += 1

    for i in range(len(res)):
        if res[i]:
            print(i, res[i])