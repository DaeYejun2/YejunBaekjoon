import sys
input = sys.stdin.readline

#5층이니까, 5층 부터 시작해서, 범위를 0<= 범위<i   (i는 층) 이렇게 해서, 
# 아래에서부터 위로 올라가는 느낌으로 2차원 배열 해당 자리의 최대값

n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int,input().split())))
    
for i in range(n-2, -1, -1):    #3~0 
    for j in range(len(tri[i])):  #0~3
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
        
print(tri[0][0])