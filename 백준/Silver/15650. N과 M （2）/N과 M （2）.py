n, m = map(int, input().split())

data = []

def back(start):
    if len(data) == m:
        print(' '.join(map(str, data)))
        return
    
    for i in range(start, n+1):
        if i not in data:
            data.append(i)
            back(i)
            data.pop()

back(1)