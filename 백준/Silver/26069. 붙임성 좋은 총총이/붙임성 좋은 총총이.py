import sys
input = sys.stdin.readline
n = int(input())
# 춤추는 사람을 만나면(set에 있는 사람 이라면) set에 추가
dance = set()

for i in range(n):
    command = list(map(str, input().rstrip().split()))
    if command[0] == 'ChongChong':
        dance.add(command[1])
    elif command[1] == 'ChongChong':
        dance.add(command[0])
    elif command[0] in dance:
        dance.add(command[1])
    elif command[1] in dance:
        dance.add(command[0])
        
print(len(dance)+1)