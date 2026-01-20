import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

for i in range(m):
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    a, b = a+b, a+b
    heapq.heappush(data, a)
    heapq.heappush(data, b)
    
print(sum(data))