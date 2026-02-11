def solution(n):
    data = []
    while n != 0:
        data.append(n%3)
        n //= 3
    res = 0; idx = 0
    for i in data[::-1]:
        res += i * (3**idx)
        idx += 1
    return res