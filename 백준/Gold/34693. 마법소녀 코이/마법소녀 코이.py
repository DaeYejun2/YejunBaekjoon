import sys
input = sys.stdin.readline

t = int(input())

def solve(k):
    res = []

    found = False
    for a in range(1,101):
        target = k-a**2
        if target > 0 and target % 2 == 1:
            c = (target-1) // 2
            if c >= 1:
                res.append(f"{a} + {c+1} - {c}")
                found = True; break
        
        target = k + a**2
        if target % 2 == 1:
            c = (target-1)//2
            if c >= 1:
                res.append(f"{c+1} - {c} - {a}")
                found = True; break
            
    print('\n'.join(res))


for i in range(t):
    solve(int(input()))