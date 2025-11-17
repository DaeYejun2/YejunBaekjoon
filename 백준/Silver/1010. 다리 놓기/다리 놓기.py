import sys
input = sys.stdin.readline
def factorial(n):
    f = 1
    for i in range(n,1,-1):
        f *= i
    return f
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    result = int(factorial(m)/(factorial(m-n)*factorial(n)))
    print(result)