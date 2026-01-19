import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    tmp_max=  0
    ans = 0
    for i in range(n-1, -1, -1):
        if data[i] > tmp_max:
            tmp_max = data[i]
        else:
            ans += tmp_max-data[i]
    print(ans)