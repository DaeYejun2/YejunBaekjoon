import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    s, t = map(int, input().split())
    time.append((s, t))
time.sort(key=lambda x: (x[0],x[1]))

heap = [time[0][1]]             #heap에는 끝나는 시간만 담긴다. 
for i in range(1,n):
    if heap[0] <= time[i][0]: #시작 시간과 비교. if문이 성립해야 pop을 할 수 있기 때문에, 성립하지 않으면 교실+1
        heapq.heappop(heap)
    heapq.heappush(heap,time[i][1])  #if문 성립하면 pop->push. 교실 수 그대로. 성립 안하면 push. 교실 수 +1

print(len(heap))