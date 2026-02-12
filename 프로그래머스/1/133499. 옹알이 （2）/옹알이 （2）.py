def solution(babbling):
    data = ["aya", "ye", "woo", "ma"]
    data1 = ["aya"*2, "ye"*2, "woo"*2, "ma"*2]
    
    cnt=0
    for b in babbling:
        no_double = True
        
        for double in data1:
            if double in b:
                no_double = False
                
        if no_double:
            word = b
            for d in data:
                word = word.replace(d, ' ')
        
            if word.strip()=='':
                cnt += 1
            
    return cnt