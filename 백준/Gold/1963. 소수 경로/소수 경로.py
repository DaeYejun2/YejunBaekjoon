import sys
from collections import deque
input = sys.stdin.readline

is_prime = [True] * 10000
end = int(10000**0.5)
is_prime[0] = is_prime[1] = False
for i in range(2, end+1):
    if is_prime:
        for j in range(i*i, 10000, i):
            is_prime[j] = False

def bfs(start, target):
    queue = deque([(start, 0)])
    visited = [False] * 10000
    visited[start] = True
    
    while queue:
        curr, count = queue.popleft()

        if curr == target:
            return count
        
        str_num = list(str(curr))
        for i in range(4):
            original = str_num[i]
            for j in range(10):
                if i == 0 and j == 0: continue

                str_num[i] = str(j)
                next_num = int("".join(str_num))

                if is_prime[next_num] and not visited[next_num]:
                    queue.append((next_num, count + 1))
                    visited[next_num] = True

            str_num[i] = original

    return "Impossible"
    

t = int(input())
for _ in range(t):
    start, target = map(int, input().split())
    print(bfs(start, target))