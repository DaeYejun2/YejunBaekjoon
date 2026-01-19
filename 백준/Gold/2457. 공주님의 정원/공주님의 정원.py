import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

i = 0; result = 0
latest_end = (3, 1)  #최근에 심은 꽃이 지는 날짜 설정

while i < n:
    sm, sd, em, ed = data[i]
    if (sm,sd) <= latest_end < (em,ed):  #당연히 이 범위 안에 있어야 꽃이 이어지겠죠(초기값)
        max_end = (em, ed)               #가장 늦게까지 꽃이 살아있는 날
        while i < n-1:                   #다음 날을 탐색해야 하기 때문에 n-1로 설정
            nsm, nsd, nem, ned = data[i+1]
            if latest_end < (nsm, nsd):
                break
            if max_end < (nem, ned):
                max_end = (nem, ned)
            i+=1
        
        result += 1
        latest_end = max_end
        
        if (11,30) < latest_end:
            print(result)
            exit(0)
    i+=1
print(0)