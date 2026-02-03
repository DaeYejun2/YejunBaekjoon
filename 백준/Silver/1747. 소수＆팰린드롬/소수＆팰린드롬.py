import sys
input = sys.stdin.readline

def prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def palindrom(n):
    l = str(n)
    if l == l[::-1]: return True
    return False

n = int(input())
while True:
    if palindrom(n) and prime(n):
        print(n)
        break
    n += 1