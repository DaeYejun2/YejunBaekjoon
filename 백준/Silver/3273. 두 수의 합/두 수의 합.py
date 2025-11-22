import sys
input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split())) #서로 다른 수를 입력 받기 때문에 set 사용하면 in 연산이 거의 O(1)이 됨
x = int(input())
cnt = 0

for i in data:
    tmp = x - i
    if tmp in data:
        cnt += 1

print(cnt//2)
#다른 코드 찾아보니 투포인터로 왼쪽에서, 오른쪽에서 서로 마주칠때까지 찾는 이분 탐색도 좋을 듯