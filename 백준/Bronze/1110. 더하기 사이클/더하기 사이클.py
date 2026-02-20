import sys
input = sys.stdin.readline

n = input().rstrip()
tmp = n
res = 0

if int(n) < 10:
    tmp = '0'+n

while True:
    tmp = tmp[1]+str((int(tmp[0])+int(tmp[1]))%10)
    res += 1
    if tmp != '' and int(n) == int(tmp): break

print(res)