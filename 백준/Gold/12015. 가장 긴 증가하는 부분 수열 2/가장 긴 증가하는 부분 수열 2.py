import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

tails = []

for x in data:
    if not tails or x > tails[-1]:
        tails.append(x)
    else:
        start = 0
        end = len(tails)

        while start < end:
            mid = (start+end)//2
            if x > tails[mid]:
                start = mid+1
            else:
                end = mid
        tails[end] = x
    
print(len(tails))