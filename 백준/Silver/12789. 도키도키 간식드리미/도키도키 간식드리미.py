import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input())
    queue_list = list(map(int, input().split()))
    queue = deque(queue_list)
    stack = []
    
    num = 1

    while queue:
        # 1. 스택에서 연속으로 꺼낼 수 있는 번호는 모두 꺼낸다.
        #    => num이 스택의 맨 위와 같을 때까지 반복
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        
        # 2. 큐의 맨 앞 번호와 현재 목표 번호(num)를 비교한다.
        current_person = queue[0]
        
        if current_person == num:
            # 2-1. 큐의 맨 앞이 목표 번호이면: 큐에서 꺼내고, num 증가
            queue.popleft()
            num += 1
            # (num이 증가했으므로 다음 반복에서 다시 스택 확인)
            
        else:
            # 2-2. 큐의 맨 앞이 목표 번호가 아니면: 스택에 넣고, 다음 큐의 번호를 확인
            # 단, 스택에 넣기 전에 현재 스택을 모두 확인하는 것이 중요
            # (위의 while stack... 에서 이미 확인했음)
            
            # 스택의 맨 위 번호보다 현재 큐의 번호가 더 크다면
            # 이는 'Nice'가 될 가능성이 아직 있음.
            # 하지만 큐에서 스택으로 넘어가는 번호는 스택의 맨 위 번호보다 작으면 안 됩니다.
            # * 이 문제에서는 번호 순서가 중요하며, 스택은 나중에 순서가 될 번호를 임시 보관하는 용도입니다.
            #   **"스택에 넣는 행위 자체"가 가능한지 불가능한지 검사할 필요는 없습니다.**
            #   단지, 큐에서 맨 앞 번호를 빼서, 목표 번호가 아니면 스택에 넣는 것이 로직입니다.
            
            stack.append(queue.popleft())

    # 3. 큐가 모두 비었으면, 스택에 남은 번호들을 순서대로 모두 꺼낸다.
    #    (이 부분은 기존 코드와 동일)
    while stack and stack[-1] == num:
        stack.pop()
        num += 1
        
    # 4. 최종 결과 확인: 스택이 비어 있어야 순서대로 모두 처리가능 ('Nice')
    if not stack:
        print("Nice")
    else:
        print("Sad")

solve()