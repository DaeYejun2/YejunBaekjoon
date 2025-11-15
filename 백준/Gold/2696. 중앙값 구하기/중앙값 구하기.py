import sys
import heapq
input = sys.stdin.readline

t = int(input())

for i in range(t):
    m = int(input())
    data = []
    for _ in range(m//10 + 1):
        data += list(map(int, input().split()))
    maxheap = []
    minheap = []
    result = [data[0]]      #i가 1부터 시작하니까
    mid = data[0]           #초기값을 mid 값으로
    
    for i, num in enumerate(data[1:], 1):        #i는 1부터, num은 num[1]부터 슬라이싱
        if num < mid:
            heapq.heappush(maxheap, -num)
        else:
            heapq.heappush(minheap, num)
        
        if i % 2 == 0:      # 인덱스가 0부터시작해서짝수인 경우 발동
            if len(maxheap) > len(minheap):
                heapq.heappush(minheap, mid)
                mid = -heapq.heappop(maxheap)
            elif len(minheap) > len(maxheap):
                heapq.heappush(maxheap,-mid)
                mid = heapq.heappop(minheap)
            result.append(mid)
#여기까지 정리하면,mid를 기준으로 큰 값은 최소힙, 작은 값은 최대 힙에 삽입.
#짝수 인덱스(문제상으론 홀수)가 되면, 길이가 더 작은 힙에 mid값 추가하고, 새로운 미드 값을 길이가 더 긴 쪽 힙에서 가져옴.
#그러면 소름 돋게도 중앙값이 나옴            
    print(m//2 + 1)
    
    for i, num in enumerate(result):
        if i != 0 and i % 10 == 0:
            print()
        print(num, end=' ')
    print()