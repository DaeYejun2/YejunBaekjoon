import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
#운동을 N분, 초기 맥박은 m, 맥박이 M보다 작거나 같을 때, 운동 1분에 +T, 쉬면 -R
tmp = m
tot = cnt = 0

while cnt < N:
    if m + T > M:
        break
    if tmp + T <= M:
        tmp += T
        cnt += 1
    else:
        tmp = max(tmp-R, m)
    tot+=1
    
print(tot if cnt==N else -1)