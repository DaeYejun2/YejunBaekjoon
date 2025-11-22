import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
data = []
arr = ['0'] * n
for x in list(map(int, input().split())):
    data.append((x, cnt))
    cnt += 1
stack = []

for x in data:
    while stack:
        if stack[-1][0]<= x[0]: #자기보다 작으면 pop
            stack.pop()
        else:
            arr[x[1]] = str(stack[-1][1] + 1)
            break
    stack.append(x)

print(' '.join(arr))

#모노토닉 스택