import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

#해당 인덱스가 가질 수 있는 최대 값.
#만약 전 인덱스(전 인덱스까지 합했을 때 가질 수 있는 최대 값)와 현재 인덱스를 더한 값보다
#현재 인덱스가 더 크다면, 그 전까지의 합은 필요 없으니, 인덱스 변경X
for i in range(1, n):
    m[i] = max(m[i], m[i]+m[i-1])
    
print(max(m))