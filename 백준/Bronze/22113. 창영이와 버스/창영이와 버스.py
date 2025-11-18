import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bus = list(map(int, input().split()))
pay = [list(map(int,input().split())) for _ in range(n)]
result = 0
for i in range(m):
    if i+1 == m: break
    result += pay[bus[i]-1][bus[i+1]-1]
    
print(result)