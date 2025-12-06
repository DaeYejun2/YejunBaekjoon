import sys
input = sys.stdin.readline

s = input().rstrip()
dict = {}
ans = 0

for i in range(len(s)+1):
    for j in range(i):
        dict[s[j:i]] = 1
            
print(len(dict))