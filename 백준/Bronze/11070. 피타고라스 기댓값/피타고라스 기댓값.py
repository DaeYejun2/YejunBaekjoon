import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())    #n은 팀 개수, m은 전체 경기 수
    team = [[0, 0] for _ in range(n+1)]    #이차원 행렬로, 1번팀(x득점, y실점)
    for j in range(m):
        a, b, p, q = map(int, input().split())
        team[a][0] += p; team[a][1] += q
        team[b][0] += q; team[b][1] += p
    ans = []
    for j in range(1, n+1):
        if team[j][0]+team[j][1] == 0:
            ans.append(0)
        else:
            w = ((team[j][0]**2) / ((team[j][0]**2) + (team[j][1]**2))) * 1000
            ans.append(int(w))
        
    print(max(ans))
    print(min(ans))