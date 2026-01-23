import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
x = []

for i in range(n-1):
    x.append(data[i+1]-data[i])
x.sort()

print(sum(x[:n-k]))