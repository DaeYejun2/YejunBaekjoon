def solution(price, money, count):
    t = 0
    for i in range(1, count+1):
        t += price*i
        
    if t > money: return t - money 
    return 0