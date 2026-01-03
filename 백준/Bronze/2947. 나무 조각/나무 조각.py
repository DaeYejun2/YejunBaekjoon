import sys
input = sys.stdin.readline

#버블 소트해서 스왑할때마다 프린트

data = list(map(int, input().split()))

for i in range(4, 0, -1):
    for j in range(0, i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            print(' '.join(map(str, data)))