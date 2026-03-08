import sys
input = sys.stdin.readline

n = int(input())

left = 1
right = n

while left <= right:
    mid = (left+right)//2

    if mid**2 == n:
        print(mid)
        break
    if mid**2<n:
        left = mid + 1
    else:
        right = mid - 1