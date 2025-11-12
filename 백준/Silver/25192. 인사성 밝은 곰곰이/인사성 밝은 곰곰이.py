import sys
input = sys.stdin.readline

n = int(input())

arr = set()
ac = 0

for i in range(n):
    command = input().rstrip()
    if command == 'ENTER':
        ac += len(arr)
        arr.clear()
    else:
        arr.add(command)
        
print(ac+len(arr))