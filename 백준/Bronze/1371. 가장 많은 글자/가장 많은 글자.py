import sys

data = sys.stdin.read()

arr = [0] * 26

for d in data:
    # 소문자인 경우에만 카운트 (공백, 줄바꿈 제외)
    if 'a' <= d <= 'z':
        arr[ord(d) - ord('a')] += 1

m = max(arr)
for i in range(len(arr)):
    if arr[i] == m:
        print(chr(97+i),end='')