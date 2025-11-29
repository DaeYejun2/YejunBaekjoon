import sys
input = sys.stdin.readline

n = int(input())

def rec(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    stars = rec(n//2)
    L = []
    
    for star in stars:
        L.append(' '*(n//2)+star+' '*(n//2))
    for star in stars:
        L.append(star+' '+star)
    return L        


print('\n'.join(rec(n)))

