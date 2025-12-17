import sys

# 입력 받기
n, k_size = map(int, sys.stdin.readline().split())
k_list = list(map(int, sys.stdin.readline().split()))

# 큰 순서대로 시도하기 위해 정렬 (필수는 아니지만 효율적일 수 있음)
k_list.sort(reverse=True)

max_val = 0

def solve(current_num):
    global max_val
    
    # 1. 현재 숫자가 N보다 크면 중단
    if current_num > n:
        return
    
    # 2. 현재 숫자가 N 이하이면 최댓값 갱신
    if current_num <= n:
        max_val = max(max_val, current_num)
    
    # 3. 집합 K의 원소들을 하나씩 붙여서 다음 숫자 생성
    for num in k_list:
        # 기존 숫자에 10을 곱하고 새 숫자를 더함 (예: 1 -> 15 -> 157)
        next_num = current_num * 10 + num
        
        # 다음 숫자가 N보다 커질 가능성이 있어도 일단 재귀 호출
        # (자릿수가 N과 같아질 때까지만 탐색하게 됨)
        if next_num <= n:
            solve(next_num)
        # 팁: k_list가 내림차순 정렬되어 있다면, 
        # next_num이 n보다 작을 때 solve를 호출하고 바로 다음 숫자로 넘어가는 식으로 최적화 가능

# 재귀 시작 (초기값 0)
solve(0)

print(max_val)