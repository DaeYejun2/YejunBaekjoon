import sys
input = sys.stdin.readline

#누적 합을 구해두고, 부분합으로 계산

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[i]+arr[i])

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])