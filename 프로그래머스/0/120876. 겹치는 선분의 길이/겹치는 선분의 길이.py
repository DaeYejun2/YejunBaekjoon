def solution(lines):
    table = [0] * 201 
    
    for start, end in lines:
        for i in range(start, end):
            table[i + 100] += 1
            
    res = 0
    for count in table:
        if count >= 2:
            res += 1
            
    return res