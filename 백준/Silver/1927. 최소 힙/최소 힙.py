import sys
input = sys.stdin.readline
import heapq    #임마는 최소힙만 구현해줌. 최대힙 하려면 -붙여서 입력, 출력

heap = []  # heapq 모듈은 일반 리스트를 힙으로 관리함

n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else: print(0)
        
    else:
        heapq.heappush(heap, x)