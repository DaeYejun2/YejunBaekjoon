import sys
input = sys.stdin.readline

le = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    tmp = le[a-1:b]
    tmp = tmp[::-1]
    le[a-1:b] = tmp
    
print(' '.join(map(str, le)))