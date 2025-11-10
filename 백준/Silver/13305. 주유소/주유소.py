import sys
input = sys.stdin.readline

oil = 0
n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[:n-2]
min_price = min(min_price)
for i in range(n):
    if min_price == price[i]:             #첫번째 도시의 기름값이 제일 싸다면,
        oil += min_price * sum(length[i:])
        break
    else:                                  # 아니라면, 다음 도시까지만 기름 값 넣고, 다음 도시에서 또 확인
        oil += price[i] * length[i]
        
print(oil)