import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

counts = Counter(map(int, data))

result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[0][0]

print(result)