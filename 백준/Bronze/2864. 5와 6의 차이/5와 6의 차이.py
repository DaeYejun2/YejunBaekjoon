import sys
input = sys.stdin.readline

a,b = input().rstrip().split()
max_a = ''; min_a = ''
max_b = ''; min_b = ''

for i in a:
    if i == '5' or i == '6':
        max_a += '6'
        min_a += '5'
    else:
        max_a += i
        min_a += i

for i in b:
    if i == '5' or i == '6':
        max_b += '6'
        min_b += '5'
    else:
        max_b += i
        min_b += i

print(int(min_a)+int(min_b),int(max_a)+int(max_b))