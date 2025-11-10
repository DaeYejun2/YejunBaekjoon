import sys
input = sys.stdin.readline

oil = 0
n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

minPrice=price[0]

for i in range(n-1):
    if minPrice > price[i]:
        minPrice = price[i]
        
    oil += minPrice*length[i]

print(oil)