def solution(food):
    for i in range(1, len(food)):
        food[i] = str(food[i]//2)
    res = ''
    print(food)
    for i in range(1, len(food)):
        print(i, food[i])
        tmp = ''
        for j in range(int(food[i])):
            tmp += str(i)
        res += tmp
    return (res + '0' + res[::-1])