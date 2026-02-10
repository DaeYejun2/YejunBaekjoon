import sys
input = sys.stdin.readline

k = int(input())
comm = list(map(str, input().rstrip().split()))
data = []
max_value = [-1]
min_value = [9999999999]

def back(idx):
    if len(data) == k+1:
        if max_value[0] < int(''.join(map(str, data))):
            max_value[0] = int(''.join(map(str, data)))
        if min_value[0] > int(''.join(map(str, data))):
            min_value[0] = int(''.join(map(str, data)))
        return
    
    if len(data) == 0:
        for i in range(0, 10):
            data.append(i)
            back(0)
            data.pop()

    if comm[idx] == '<':
        for j in range(0, 10):
            if len(data) != 0 and j not in data and j > data[idx]:
                data.append(j)
                back(idx+1)
                data.pop()
    else:
        for l in range(0, 10):
            if len(data) != 0 and l not in data and l < data[idx]:
                data.append(l)
                back(idx+1)
                data.pop()

back(0)
if max_value[0] < 10**(k): print('0'+str(max_value[0]))
else: print(*max_value)
if min_value[0] < 10**(k): print('0'+str(min_value[0]))
else: print(*min_value)