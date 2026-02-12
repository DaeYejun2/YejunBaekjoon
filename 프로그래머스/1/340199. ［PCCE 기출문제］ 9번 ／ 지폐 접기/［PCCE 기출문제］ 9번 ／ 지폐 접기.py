def solution(wallet, bill):
    if wallet[0]<wallet[1]:wallet[0],wallet[1] = wallet[1],wallet[0]
    if bill[0]<bill[1]:bill[0],bill[1] = bill[1],bill[0]
    cnt = 0
    while (bill[1] > wallet[1]) or (bill[0] > wallet[0]):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        cnt += 1
        if bill[0]<bill[1]:bill[0],bill[1] = bill[1],bill[0]
    return cnt