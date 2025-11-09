# 1. -가 3N개 있는 문자열에서 시작한다.

# 2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다. 이렇게 하면, 선(문자열) 2개가 남는다.

# 3. 이제 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다. 이 과정은 모든 선의 길이가 1일때 까지 계속 한다.
import sys
input = sys.stdin.readline
while True:
  try:
    
    n = int(input())

    if n == 0: print('-',end='')

    n = 3**n
    
    def rec(a, b):
      if b < 0: return
      m = (b-a+1) // 3
      if a % 2 == 1:  #홀수면
        for i in range(a, b+1):
          print(' ',sep='',end='')
      else:
        if a == b:
          print('-',sep='',end='')
        rec(0, m-1)
        rec(m, 2*m-1)
        rec(2*m, 3*m-1)
        return
          

    rec(0, n)
    print()
  
  except:
    break