import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = sorted(list(map(int, input().split())))
x = []

for i in range(n-1):
    x += [data[i+1]-data[i]]
x.sort()
print(sum(x[:n-k]))  # 가장 거리가 긴 k개의 도로만 연결 안하면 됨