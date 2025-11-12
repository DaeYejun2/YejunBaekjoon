import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dic = dict()

for i in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
#알파벳, 단어 길이, 등장횟수
d = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in d:
    print(i[0])