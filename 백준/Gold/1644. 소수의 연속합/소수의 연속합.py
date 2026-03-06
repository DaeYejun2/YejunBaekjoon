import sys
input = sys.stdin.readline

n = int(input())

prime = [True]*(n+1)
prime[0]=prime[1]=False

for i in range(2,int(n**0.5)+1):
    for j in range(i*i,n+1,i):
        prime[j]=False
arr = []
for i,p in enumerate(prime):
    if p:
        arr.append(i)
res = 0

for i in range(len(arr)):
    tmp = 0
    for j in range(i,len(arr)):
        tmp += arr[j]
        if tmp == n: 
            res += 1
            break
        elif tmp > n:
            break
        
print(res)