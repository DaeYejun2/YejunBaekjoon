#1. 첫번째 원소 뽑아내기. 그냥 popleft
#2. 왼쪽으로 한칸 이동. popleft한거를 append 뒤로 보내기
#3. 오른쪽으로 한칸 이동. pop한거를 appendleft
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
q = deque()
for i in range(1, n+1):
    q.append(i)

for x in data:
    mid = (len(q) - 1)//2
    i, j = 0, len(q)-1
    cnti, cntj = 0, 1
    while x != q[i] and i <= mid:
        i += 1
        cnti += 1
    while x != q[j] and j >= mid:
        j -= 1
        cntj += 1
    
    if cnti < cntj:   #2. 왼쪽으로 한칸 이동. popleft한거를 append/ 뒤로 보내기
        while i:
            q.append(q.popleft())
            i -= 1
    else:
        while j != len(q):    #3. 오른쪽으로 한칸 이동. pop한거를 appendleft / 앞으로 보내기
            q.appendleft(q.pop())
            j += 1
    q.popleft()
    cnt += min(cnti, cntj)
    
print(cnt)