import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num = int(input())
    max_ = 1
    while num != 1:
        max_ = max(max_, num)
        if num % 2:
            num = 3*num + 1
        else:
            num //= 2
        
    print(max_)