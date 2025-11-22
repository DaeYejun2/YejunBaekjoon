import sys
from collections import deque

#n+1 개의 I로 이루어져 있고 n개의 O로 이루어져 있다
#1,000,000만에 제한 1초 니까 n 혹은 nlogn이 최선

# 2
# 13
# OOIOIOIOIIOII

#I가 나오면 덱에 집어 넣고, O가 아니면 pop, I니까 다시 넣고 이런식으로 덱에 IOIOI가 완성이 되면 pop두번 하고 다시
n = int(input())
m = int(input())
data = input().rstrip()
tmp = 'IOI'
for _ in range(n-1):
    tmp += 'OI'
q = deque()
cnt = 0
result = 0

for x in data:
    if x == 'I':  #I일때 q의 이미들어와  있는 값이 I라면 popleft IOI일때 I가 들어와 IOII 다 pop?
        if not q: #q가 비어 있다면
            q.append('I')
            cnt += 1
        elif q[-1] == 'I':
            while q:
                q.popleft()
            q.append('I')
            cnt = 1
        else:
            q.append('I')
            cnt += 1
    else:  #O라면,  IO일때 O가 들어온다 다 pop
        if not q: #q에 뭐가 없으면 컨티뉴
            continue
        elif q[-1] == 'I':  # 마지막값이 I면 append
            q.append('O')
            cnt += 1
        else:               #마지막 값이 O면 초기화
            while q:
                q.popleft()
                cnt = 0          
    if cnt == 2*n + 1:
        result+=1
        q.popleft()
        q.popleft()
        cnt -= 2
        
print(result)