import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
l, r = 0, 0
ans = 0

while r < n:
    k = sum(data[l:r+1])
    if k == m:
        ans += 1
        r += 1
    elif k > m:
        l += 1
    else:
        r += 1
        
print(ans)