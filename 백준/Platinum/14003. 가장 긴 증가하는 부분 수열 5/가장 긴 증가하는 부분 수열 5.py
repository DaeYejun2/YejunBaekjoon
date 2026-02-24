import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

tails = []
pre = [0]*n

for i, x in enumerate(data):
    if not tails or x > tails[-1]:
        tails.append(x)
        pre[i] = len(tails)-1
    else:
        left, right = 0, len(tails)
        while left<right:
            mid = (left+right)//2
            if x > tails[mid]:
                left=mid+1
            else:
                right = mid
        tails[right]=x
        pre[i] = right

m = max(pre)
print(m+1)
res = []
for i in range(n-1,-1,-1):
    if pre[i] == m:
        res.append(data[i])
        m-=1

print(*res[::-1])