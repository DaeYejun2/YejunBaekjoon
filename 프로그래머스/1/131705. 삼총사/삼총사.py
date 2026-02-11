data = []
cnt = [0]
def back(number, start):
    if len(data) == 3:
        if sum(data) == 0: 
            cnt[0] += 1
        return
    
    for i in range(start, len(number)):
        data.append(number[i])
        back(number, i+1)
        data.pop()

def solution(number):
    back(number, 0)
    return cnt[0]
        
