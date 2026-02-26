import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * k
    for i in range(k):
        cmd, n = input().split()
        num = int(n)

        if cmd == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True # 일단 유효하다고 표시

        elif cmd == 'D':
            if num == 1: # 최댓값 삭제 중에서
                # 이미 삭제된 (유효하지 않은) 값들은 힙에서 먼저 제거
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False # 삭제 처리
                    heapq.heappop(min_heap)

    # 모든 연산 후, 다시 한 번 유효하지 않은 값 걷어냄
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])