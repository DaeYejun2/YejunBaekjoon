import sys
import heapq
input = sys.stdin.readline

# 무게는 가방이 담을 수 있는 무게 확인용, 담을 수 있는 애들 중 가장 비싼애
heap = []
result = 0
gems = []

n, k = map(int,input().split())
for i in range(n):
    m, v = map(int,input().split())
    gems.append((m, v))
# 무게를 기준으로 먼저 정렬

bags = [int(input()) for _ in range(k)]
gems.sort();bags.sort()

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(heap, -gems[0][1])
        heapq.heappop(gems)
    if heap:
        result -= heapq.heappop(heap)
        
print(result)