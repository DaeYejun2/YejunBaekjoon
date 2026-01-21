import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))
    
data.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    if i == 0: 
        a, b = data[0]
        ans = abs(b-a)
    else:
        if b >= data[i][0]:
            if not b >= data[i][1]:
                b = data[i][1]
                ans += abs(b-a)
        else:
            a, b = data[i]
            ans += abs(b-a)
    a = b

print(ans)