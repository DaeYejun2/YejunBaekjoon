import sys
input = sys.stdin.readline

char_to_int = {}
for i in range(10):
    char_to_int[str(i)] = i
for i in range(26):
    char_to_int[chr(i+ord('A'))] = i+10

int_to_char = {v: k for k, v in char_to_int.items()}

n = int(input())
data = []
for _ in range(n):
    data.append(input().rstrip())
k = int(input())

# 각 문자를 Z로 바꿨을 때의 추가 이득을 저장할 리스트
diffs = [0]*36
total_sum = 0

for d in data:
    le = len(d)
    for i, char in enumerate(d):
        val = char_to_int[char]
        # 자릿수 (오른쪽 끝이 36^0)
        power = le - i - 1
        place_val = 36** power

        total_sum += val*place_val # N개의 수를 다 더한다

        # 이 문자를 Z로 바꿨을 때 얻는 이득
        diffs[val] += (35-val)*place_val

# 이득이 큰 순서대로 정렬
diffs.sort(reverse=True)

# 최대 K개까지 본 이득도 다 더한다
for i in range(k):
    total_sum += diffs[i]

if total_sum == 0:
    print(0)

else:
    res = []
    while total_sum > 0:
        res.append(int_to_char[total_sum%36])
        total_sum //= 36

    print(''.join(reversed(res)))