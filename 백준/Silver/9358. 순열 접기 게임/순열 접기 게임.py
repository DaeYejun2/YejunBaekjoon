import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))

    while len(data) > 2:
        le = []
        half = (len(data) + 1) // 2
        for j in range(half):
            le.append(data[j]+data[len(data)-1-j])
        data = le
        
    result = "Alice" if data[0] > data[1] else "Bob"
    print(f"Case #{i+1}: {result}")