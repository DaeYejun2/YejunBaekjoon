import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    command = list(map(int, input().split()))
    if command[0] == 0: break
    else:
        for i in combinations(command[1:], 6):
            print(' '.join(map(str, i)))
    print()