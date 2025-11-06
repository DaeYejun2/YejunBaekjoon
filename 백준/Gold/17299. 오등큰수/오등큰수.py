import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
max_val = max(arr)

stack = []
cnt = [0] * (max_val + 1)
result = [-1] * n

for i in range(n):
    cnt[arr[i]] += 1                    #개수 정렬할거면 cnt 초기화 하고 해야 됨

for i in range(n):
    while stack and cnt[arr[i]] > cnt[arr[stack[-1]]]:     # arr[i]가 1이면 스택에 저장된 인덱스를 꺼내서 cnt에 넣어서 확인을 한다.
        j = stack.pop()                     #작으면 스택에 들어가는데, 오등큰수를 만났으니 작은 인덱스가 pop되고, 거기에 arr[i]를 넣는다.
        result[j] = arr[i]
    stack.append(i)
    
print(*result)      