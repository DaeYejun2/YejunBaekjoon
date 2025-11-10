import sys
input = sys.stdin.readline

k, n = map(int, input().split())
order = []

for i in range(k):
    order.append(int(input()))

left, right = 1, max(order)
result = 0

while left <= right:
    middle = (left + right) // 2
    total = 0
    for i in order:
        total += i // middle

    if total >= n:
        left = middle + 1
        result = middle
    else:
        right = middle - 1
        
print(result)