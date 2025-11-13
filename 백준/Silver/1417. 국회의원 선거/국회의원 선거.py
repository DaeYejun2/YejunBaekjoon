import sys
input = sys.stdin.readline
arr = []
n = int(input())
cnt = 0

for i in range(n):
    arr.append(int(input()))
    
#for문 돌리면서 max값 인덱스 얻고, 해당 인덱스 값 하나 줄이고 다솜이 올리기. 
#그렇게 다솜이가 max가 될때까지. 그러고 +1. 동점인 경우가 있으니

while arr[0] <= max(arr):
    max_v = arr[0]
    max_idx = 0
    for i in range(0,n):
        if max_v <= arr[i]: 
            max_v = arr[i]
            max_idx = i
    if max_idx == 0: break
    else:
        arr[max_idx] -= 1
        arr[0] += 1
        cnt += 1
    
print(cnt)