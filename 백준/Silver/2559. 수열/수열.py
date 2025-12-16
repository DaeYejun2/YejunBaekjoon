import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

prefix = [sum(data[0:k])]

for i in range(0, n-k):
    prefix.append(prefix[i]-data[i]+data[i+k])
    
print(max(prefix))