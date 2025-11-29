import sys
input = sys.stdin.readline

n = int(input())

def rec(n):
    if n == 1:
        return ['*']
    
    stars = rec(n//3)
    L = []
    
    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star+' '*(n//3)+star)
    for star in stars:
        L.append(star*3)
        
    return L

print('\n'.join(rec(n)))

#레전드 이해. 처음에 [***, * *, ***]이 만들어 지는 것은 이해가 될 것이다. 근데 갑자기 어떻게 9개가 되느냐 의아해 할 것이다. 내가
#그 이유는 저 배열을 리턴하기 때문에 stars의 배열은 * 에서 ***, * *, ***로 변하게 된다. 이 배열로 for문 돌리면서 또 L에 저장하면
#아래와 같은 형태가 나오게 된다.

# 9
# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********