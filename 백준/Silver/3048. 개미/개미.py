import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())

s1 = list(input().rstrip())[::-1]
s2 = list(input().rstrip())

ants = []
for char in s1:
    ants.append([char, 1])
for char in s2:
    ants.append([char, 2])

t = int(input())

for _ in range(t):
    i = 0
    while i < len(ants) - 1:
        # 현재 개미가 그룹 1(오른쪽행)이고, 다음 개미가 그룹 2(왼쪽행)인 경우
        if ants[i][1] == 1 and ants[i+1][1] == 2:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            # 자리를 바꾼 개미가 이번 초에 또 바뀌면 안 되므로 한 칸 더 건너뜀
            i += 1
        i += 1

print("".join([ant[0] for ant in ants]))