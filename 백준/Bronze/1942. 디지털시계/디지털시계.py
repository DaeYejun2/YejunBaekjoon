import sys
input = sys.stdin.readline

for _ in range(3):
    start, end = input().strip().split()
    h1, m1, s1 = map(int, start.split(':'))
    h2, m2, s2 = map(int, end.split(':'))
    cnt = 0
    
    while True:
        if s1 == 60: s1 = 0; m1 += 1
        if m1 == 60: m1 = 0; h1 += 1
        if h1 == 24: h1 = 0
        
        tmp = 10000 * h1 + 100*m1 + s1
        if tmp % 3 == 0: cnt += 1
        if s1 == s2 and m1 == m2 and h1 == h2:
            break
        s1 += 1
    
    print(cnt)