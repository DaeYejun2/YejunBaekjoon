def func(n):
    tmp = 0
    for j in range(1,int(n**0.5)+1):
        if n % j == 0:
            if j*j==n: tmp += 1
            else: tmp += 2
    return tmp

def solution(number, limit, power):
    data = [1]
    for i in range(2, number+1):
        f = func(i)
        if f > limit:
            data.append(power)
        else: data.append(f)
        
    return sum(data)