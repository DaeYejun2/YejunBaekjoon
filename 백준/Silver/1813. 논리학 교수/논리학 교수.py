import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
cnt = [0] * 51
max_ = 0

for i in data:
    cnt[i] += 1
for i in range(0, 51):
    if i == cnt[i]:
        max_ = max(max_, i)
        
print(max_ if max_ != 0 or cnt[0] == 0 else -1)