import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
left, right = 1, max(tree)
result = 0
# O(nlogn) 인거 같은디. 
while left <= right:
    mid = (left + right) // 2
    total = 0
    
    for i in tree:   # mid만큼 자른 나무의 길이     
        if i >= mid:
            total += i - mid
    if total >= m:      #너무 많이 잘랐다, 그럼 mid를 좀 키워야지
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)