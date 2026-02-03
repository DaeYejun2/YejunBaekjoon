import sys
input = sys.stdin.readline

m, n = map(int, input().split())
l = n-m+1
end = int(n**0.5)
arr = [True] * l

for i in range(2, end+1):
    squre = i * i
    
    start_idx = m // squre  # 처음으로 m이상 되는 제곱수를 찾기 위함
    if m % squre != 0:
        start_idx += 1

    for j in range(start_idx*squre, n+1, squre):
        arr[j-m] = False

print(arr.count(True))