def solution(n, arr1, arr2):
    # tmp = bin(9)[2:]
    res = []
    
    for i in range(n):
        a1 = bin(arr1[i])[2:]
        a2 = bin(arr2[i])[2:]
        if len(a1) < n:
            a1 = '0' * (n-len(a1)) + a1
        if len(a2) < n:
            a2 = '0' * (n-len(a2)) + a2
        idx = 0
        tmp = ''
        for aa1, aa2 in zip(a1, a2):
            if aa1 == '1' or aa2 == '1':
                tmp += '#'
            else:
                tmp += ' '
            idx+=1
        res.append(tmp)
    return (res)