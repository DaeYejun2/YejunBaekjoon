import sys
input = sys.stdin.readline

#B는 재배열 하면 안되고, A만 재배열 해서 S의 크기가 최소가 되게 만들기

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#a를 오름차순, B를 내림차순해서 곱하면 되는거 아닌가
a.sort()
b.sort(reverse=True)
sum = 0

for i in range(n):
    sum += a[i]*b[i]
    
print(sum)