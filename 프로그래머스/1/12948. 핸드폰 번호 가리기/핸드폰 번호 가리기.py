def solution(phone_number):
    le = len(phone_number)
    res = ''
    for i in range(le-4):
        res+='*'
    
    for i in phone_number[-4::]:
        res+=i
    
    return res