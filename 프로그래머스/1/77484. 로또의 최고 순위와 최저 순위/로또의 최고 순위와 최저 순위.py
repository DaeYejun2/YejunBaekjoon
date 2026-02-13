def solution(lottos, win_nums):
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    res = [0,0] # 최고 순위/ 최저 순위
    tmp = 0
    for l in lottos:
        if l in win_nums:
            tmp += 1
    res[0] = dic[lottos.count(0) + tmp]
    res[1] = dic[tmp]
    return res