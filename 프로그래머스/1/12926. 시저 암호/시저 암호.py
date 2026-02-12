def solution(s, n):
    res = []
    for c in s:
        if c == ' ': res.append(' ')
        elif ord('a') <= ord(c) <= ord('z'):
            if ord(c)+n > ord('z'):
                tmp = ord(c)+n - ord('z') + ord('a') -1
                res.append(chr(tmp))
            else:
                res.append(chr(ord(c)+n))
    
        else:
            if ord(c)+n > ord('Z'):
                tmp = ord(c)+n - ord('Z') + ord('A') -1
                res.append(chr(tmp))
            else:
                res.append(chr(ord(c)+n))
                
    return ''.join(res)