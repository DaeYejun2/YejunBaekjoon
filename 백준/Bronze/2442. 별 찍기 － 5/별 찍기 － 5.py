import sys
input = sys.stdin.readline


n = int(input())

for i in range(n):
    print(' ' * (n-1-i),end='')
    print('*' * (i*2+1),end='')
    print()