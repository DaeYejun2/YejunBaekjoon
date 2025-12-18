import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
for i in permutations(data, r=m):
    print(' '.join(map(str, i)))