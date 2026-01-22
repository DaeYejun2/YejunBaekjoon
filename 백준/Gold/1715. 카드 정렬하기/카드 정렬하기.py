import sys
import heapq
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n): data.append(int(input()))
heapq.heapify(data)
ans = 0
while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    ans += a+b
    heapq.heappush(data, a+b)
    
print(ans)