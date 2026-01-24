import sys
input = sys.stdin.readline
t = 1
while True:
    l, p, v = map(int, input().split())   # p일중 l일만 사용할 수 있다 l=5, p=8, v=20
    if l == 0 and p == 0 and v == 0: break
    ans = 0
    le = v//p
    for i in range(le+1):
        if v >= l:
            ans += l
        else:
            ans += v
        v = abs(v - p)
    print(f'Case {t}: {ans}')
    t += 1