import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:
        return
    
    root = data[start]
    mid = end+1 # 모든 원소가 루트노드보다 작은 경우

    for i in range(start+1, end+1):
        if data[i] > root:
            mid = i
            break

    post(start+1,mid-1) # 왼쪽 서브트리
    post(mid, end) # 오른쪽 서브트리
    print(root) # 루트 출력

post(0, len(data)-1)