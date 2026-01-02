import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    u = list(map(str, input().strip().split()))
    v = list(map(str, input().strip().split()))
    x,y = '',''
    for j in range(m):
        x += u[j]; y += v[j]
    x = int(x); y = int(y)
    dolimpan = list(map(str, input().split()))
    cnt = 0
    for j in range(n):
        s = ''
        for k in range(j, j+m):
            if k >= n: k %= n
            s += dolimpan[k]
        s = int(s)
        if s >= x and s <= y: cnt += 1
        
    print(cnt)