def solution(answers):
    a1 = [1,2,3,4,5] ;i1 = 0
    b1 = [2,1,2,3,2,4,2,5]; i2 = 0
    c1 = [3,3,1,1,2,2,4,4,5,5]; i3 = 0
    
    tmp = [0, 0, 0]
    
    for ans in answers:
        if ans == a1[i1]: tmp[0] += 1
        if ans == b1[i2]: tmp[1] += 1
        if ans == c1[i3]: tmp[2] += 1
        i1 = (i1+1) % 5
        i2 = (i2+1) % 8
        i3 = (i3+1) % 10
        
    max_t = max(tmp); res = []
    for i in range(3):
        if tmp[i] == max_t:
            res.append(i+1)
    res.sort()
    return res