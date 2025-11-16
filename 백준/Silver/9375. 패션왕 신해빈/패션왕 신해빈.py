import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    weardict = {}
    
    for i in range(n):
        wear=list(input().rstrip().split())
        if wear[1] in weardict:     #옷장 안에 있으면 wear[1]은 옷 종류
            weardict[wear[1]].append(wear[0])   # 아 종류를 하나씩 늘리려는건가 아 종류 별로 몇개 있는지 확인하려고
            #예를 들어 headhear라면 else문에서 headgear = hat 됐고, 
            #다음에 또 headgear 나오면, headgear에 turban 추가하고 그러는거네.
            # 이렇게 하면 headgear의 종류 수를 알 수 있고.
        else:
            weardict[wear[1]] = [wear[0]]
            
    cnt = 1
    
    for k in weardict:
        cnt *= len(weardict[k]) + 1
    print(cnt-1)