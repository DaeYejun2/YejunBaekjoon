def solution(num, hand):
    key ={
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    left_pos = key['*']
    right_pos = key['#']
    res = []
    
    for n in num:
        target = key[n]
        
        if n in [1,4,7]:
            res.append('L')
            left_pos = target
        elif n in [3,6,9]:
            res.append('R')
            right_pos = target
        else:
            dist_l = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            dist_r = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])
            
            if dist_l < dist_r:
                res.append('L')
                left_pos = target
            elif dist_r < dist_l:
                res.append('R')
                right_pos = target
            else:
                if hand == "left":
                    res.append('L')
                    left_pos = target
                else:
                    res.append('R')
                    right_pos = target
                    
    return "".join(res)