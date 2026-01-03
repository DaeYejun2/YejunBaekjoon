import sys
input = sys.stdin.readline

data = [0,0,0]
n = float(input())
for i in range(3):
    a, b = map(float, input().split())
    data[i] = [a, b]

for i in range(3):
    if data[i][0] == data[i][1]: continue
    tmp = (data[i][0] + data[i][1]) / 2.0     #갈라진 부분
    for j in range(i+1, 3):
        data[j][0] = abs(data[j][0] - tmp)
        data[j][1] = abs(data[j][1] - tmp)
            
    n = max(tmp, n-tmp)
    
print(n)