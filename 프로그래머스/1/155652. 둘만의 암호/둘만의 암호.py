def solution(s, skip, index):
    char = ''
    for c in s:
        tmp = ord(c)
        cnt = 0
        
        while cnt < index:
            tmp += 1
            if tmp > ord('z'):
                tmp = ord('a')
            if chr(tmp) not in skip:
                cnt += 1
        char += chr(tmp)
    return char
        

#a b c d e f g h i j k l m n o p q r s t u v w x y z