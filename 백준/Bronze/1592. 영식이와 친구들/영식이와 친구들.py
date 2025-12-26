import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
#1부터 N번까지 자리, 공 M번 받으면 끝, 받은 횟수가 홀수면 현위치서 시계 L번째, 짝수면 반시계 L번째
#공을 총 몇번 던졌는지
max_cnt = 1; tot = 0; current = 0
le = [0] * N #1번 시작이니까, 0번 시작으로 할게요
le[0] += 1

while max_cnt != M:
    if le[current] % 2:
        current = (current+L)%N
        le[current] += 1
        max_cnt = max(max_cnt, le[current])
    else: 
        current = ((current-L) + N) % N
        le[current] += 1
        max_cnt = max(max_cnt, le[current])
        
    tot += 1
    
print(tot)