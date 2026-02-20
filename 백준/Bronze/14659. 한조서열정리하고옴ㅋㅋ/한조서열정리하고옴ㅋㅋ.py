import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))
high = 0 # 제일높은 봉우리
cnt = 0
total = []

for i in data:
    if i > high:
        high=i
        cnt=0
    else:
        cnt+=1
    total.append(cnt)

print(max(total))