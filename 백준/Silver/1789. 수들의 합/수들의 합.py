import sys
input = sys.stdin.readline

n = int(input())
ans = 0; i = 1
#더한게 n을 초과하더라도 그 초과한 수 하나만 빼주면 된다.
while True:
    ans += i
    if ans > n:
        i -= 1
        break
    elif ans == n:
        break
    
    i += 1
        
print(i)