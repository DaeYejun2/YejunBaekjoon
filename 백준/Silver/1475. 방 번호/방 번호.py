import sys
input = sys.stdin.readline

n = input().rstrip()

#nlogn아니면 n 으로 ㄱㄱ

data = [0] * 10

for x in n:
    if x == '9' or x == '6':
        if data[9] > data[6]: data[6]+=1
        else: data[9] += 1
    else:
        data[int(x)] += 1
    
print(max(data))