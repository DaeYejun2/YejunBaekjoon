import sys
import itertools
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
le = len(str(n))

while True:
    a = list(itertools.product(data, repeat=le))
    result = []
    for i in a:
        temp = int(''.join(map(str, i)))
        if n >= temp:
            result.append(temp)
    if len(result) >= 1:
        print(max(result))
        break
    else:
        le -= 1