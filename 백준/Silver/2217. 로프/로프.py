import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):data.append(int(input()))
data.sort(reverse=True)
w = data[0]

for i in range(1, n):
    tmp = data[i] * (i+1)
    if tmp >= w: w = tmp
    
print(w)