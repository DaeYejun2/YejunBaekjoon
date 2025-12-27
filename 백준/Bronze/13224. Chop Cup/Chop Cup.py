import sys
input = sys.stdin.readline

#  A: 1,2교체, B: 2,3교체, C: 1,3교체

s = input().strip()
data = [1, 0, 0]

for i in s:
    if i == 'A':
        data[0], data[1] = data[1], data[0]
    elif i == 'B':
        data[1], data[2] = data[2], data[1]
    else:
        data[0], data[2] = data[2], data[0]
        
for i in range(3):
    if data[i] == 1: print(i+1)