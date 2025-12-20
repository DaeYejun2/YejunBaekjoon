import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
isused1 = [False]*40     #y의 위치. 같은 열에 있으면 안되죠
isused2 = [False]*40    #x+y 의 위치
isused3 = [False]*40    #x-y+n-1의 위치

def Queen(cur):
    global cnt
    if cur == n:
        cnt+=1
        return
    
    for i in range(n):
        if isused1[i] or isused2[cur+i] or isused3[cur-i+n-1]:
            continue
        
        isused1[i] = True
        isused2[cur+i] = True
        isused3[cur-i+n-1] = True
        Queen(cur+1)
        isused1[i] = False
        isused2[cur+i] = False
        isused3[cur-i+n-1] = False
        
Queen(0)
print(cnt)