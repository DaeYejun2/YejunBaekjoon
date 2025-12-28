import sys
input = sys.stdin.readline

N = int(input())

bucketList = [0]*1001
for i in range(N):
    si, ti, bi = map(int, input().split())
    bucketList[si] += bi # 시작 시간에는 bucket 필요 갯수만큼 더해서 표시
    bucketList[ti] -= bi # 종료 시간에는 bucket 필요 갯수만큼 빼서 표시

bucket = 0
ans = 0    

for i in range(len(bucketList)):
    bucket += bucketList[i]
    ans = max(ans, bucket)
    
print(ans)