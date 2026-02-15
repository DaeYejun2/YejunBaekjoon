def solution(n):
    arr = [[0]*i for i in range(1, n+1)]
    dirs = [(1,0), (0,1), (-1,-1)]
    x,y = 0,0
    i = 1
    turns = 0
    end_num = sum(i for i in range(1, n+1))
    
    while i <= end_num:
        arr[x][y] = i
        dx, dy = dirs[turns]
        i += 1
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            turns = (turns+1) % 3
            dx, dy = dirs[turns]
            x+=dx
            y+=dy
    ans = []
    
    for a in arr:
        for item in a:
            ans.append(item)
    return ans