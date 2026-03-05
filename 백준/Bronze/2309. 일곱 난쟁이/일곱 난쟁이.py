import sys
input = sys.stdin.readline
data=[]
for i in range(9):
    data.append(int(input()))

data.sort()
target = sum(data)-100

for i in range(9):
    for j in range(i+1, 9):
        if data[i]+data[j]==target:
            for d in data:
                if d != data[i] and d != data[j]:
                    print(d)
            exit()