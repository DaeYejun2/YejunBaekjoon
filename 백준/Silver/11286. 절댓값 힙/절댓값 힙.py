import sys
import heapq 
input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    
    if x == 0:
        if heap:
            # 튜플의 두 번째 요소 (실제 값)를 출력
            print(heapq.heappop(heap)[1]) 
        else: 
            print(0)
    else:
        # 우선순위 튜플: (절댓값, 실제 값)
        # heapq는 튜플을 비교할 때 첫 번째 요소(절댓값)로 먼저 비교하고,
        # 같으면 두 번째 요소(실제 값)로 비교하므로, 우리가 원하는 절댓값 최소 힙이 구현됩니다.
        heapq.heappush(heap, (abs(x), x))