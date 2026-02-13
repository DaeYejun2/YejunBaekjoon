n = int(input())
dic = {}
for i in range(n):
    s = input()
    if s not in dic:
        dic[s] = 1
    else: dic[s] += 1

dic = dict(sorted(dic.items()))
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

for i in dic:
    print(i)
    break