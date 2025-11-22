import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = input().rstrip()

cnt = 0
result = 0
i = 0

while i < m:
    if data[i] == 'I':
        if i + 2 < m and data[i+1] == 'O' and data[i+2] == 'I':
            cnt += 1  # IOI 패턴 하나 발견. 완성은 아님
            if cnt >= n:
                #cnt가 n차 IOI를 만족하면 결과에 1 증가
                result += 1
            i += 2 # 다음 검사를 현재 'I'의 다음 'O'를 건너뛰고, 그 다음 'I'부터
        else: # I다음에 OI가 아니면 패턴이 끊어진 것이므로 cnt 0으로
            cnt = 0
            i += 1
    else: # O가 나오면 패턴 끊어진거니까 cnt 초기화
        cnt = 0
        i += 1
print(result)