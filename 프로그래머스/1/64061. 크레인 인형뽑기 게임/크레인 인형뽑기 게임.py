def solution(board, moves):
    le = len(board)
    data = []
    for i in range(le):
        data.append([])
        for j in range(le-1, -1, -1):
            if board[j][i] != 0:
                data[i].append(board[j][i])

    stack = []
    res = 0
    for m in moves:
        if len(data[m-1]) > 0:
            tmp = data[m-1].pop()
            if stack:
                if stack[-1] == tmp: 
                    stack.pop()
                    res += 1
                else:
                    stack.append(tmp)
            else:
                stack.append(tmp)
            
        
    return res*2