string = input()

if len(string) % 5 != 0:
    print(-1)
    exit()

res = 0
quack = {'q': 0, 'u': 0, 'a': 0, 'c': 0, 'k': 0}
curr_d = 0
max_d = 0
b = False

for s in string:
    if s == 'q':
        quack[s] += 1
        curr_d += 1
        max_d = max(max_d, curr_d) # 최대 오리 수
    else:
        # 직전 문자 있는지 확인하는 코드
        prev = {'u': 'q', 'a': 'u', 'c': 'a', 'k': 'c'}[s]
        if quack[prev] > 0:
            quack[prev] -= 1
            quack[s] += 1
            if s == 'k':
                curr_d -= 1
                quack['k'] -= 1
        else:
            print(-1)
            exit()

if curr_d == 0 and max_d > 0:
    print(max_d)
else:print(-1)