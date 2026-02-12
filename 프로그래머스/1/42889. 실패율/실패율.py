def solution(N, stages):
    le = len(stages)
    stages.sort()

    idx = 0
    res = []
    for i in range(1, N+1):
        tmp = 0 # 실패한 놈
        while stages[idx] <= i:
            tmp += 1
            if idx+1 == len(stages): break
            idx += 1
        if le > 0:
            fail_rate = tmp / le
        else:
            fail_rate = 0
            
        res.append((i, fail_rate))
        le -= tmp 
        
    res.sort(key=lambda x: x[1], reverse=True)
    return [r[0] for r in res]