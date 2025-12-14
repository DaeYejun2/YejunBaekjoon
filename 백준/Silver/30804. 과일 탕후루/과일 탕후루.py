import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

left = 0; max_len = 0
fruit_cnt = {} #과일의 종류

for right in range(n):
    current = data[right]
    
    if current in fruit_cnt:
        fruit_cnt[current] += 1
    else:
        fruit_cnt[current] = 1
    while len(fruit_cnt) > 2:
        remove = data[left]
        fruit_cnt[remove] -= 1
        if fruit_cnt[remove] == 0:
            del fruit_cnt[remove]
        left += 1
        
    max_len = max(max_len, right - left + 1)
    
print(max_len)