import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [0]
すごろく = []
current = 1
ans = 0

for i in range(n):
    d = int(input())
    l.append(d)

for i in range(m):
    d = int(input())
    すごろく.append(d)
    
for i in range(m):
    if current + すごろく[i] < n:
        current += すごろく[i]
    else:
        ans = i+1
        break
    if current + l[current] < n:
        current += l[current]
    else:
        ans = i+1
        break
    
print(ans)