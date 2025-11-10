import sys
input = sys.stdin.readline

n = int(input())
office = []
cnt = 1

for i in range(n):
    office.append(list(map(int, input().split())))
    
office = sorted(office, key = lambda x: (x[1],x[0]))
endpoint = office[0][1]   #끝나는 시간을 지정해놓고

for i in range(1, n):
    if endpoint <= office[i][0]:
        endpoint = office[i][1]
        cnt += 1

print(cnt)