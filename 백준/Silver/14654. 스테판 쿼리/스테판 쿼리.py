import sys
input = sys.stdin.readline

n = int(input())
# 가위가 1 바위가 2 보가 3
team1 = list(map(int, input().split())); cnt1 = 0
team2 = list(map(int, input().split())); cnt2 = 0
max_ = 0

def match(a, b):
    if (a-1) == b%3: return a
    elif (b-1) == a%3: return b
    else: return False
    
for i in range(n):
    if match(team1[i], team2[i]) == team1[i]: cnt1 += 1; cnt2 = 0
    elif match(team1[i], team2[i]) == team2[i]: cnt2 += 1; cnt1 = 0
    else:
        if cnt1 == 0: cnt1 += 1; cnt2 = 0
        elif cnt2 == 0: cnt2 += 1; cnt1 = 0
    max_ = max(max_, cnt1)
    max_ = max(max_, cnt2)
    
print(max_)