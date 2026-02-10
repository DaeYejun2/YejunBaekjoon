import sys
input = sys.stdin.readline

k = int(input())
signs = input().split()

visited = [False] * 10
results = []

def check(a, b, op):
    if op == '<':
        return a < b
    return a > b

def solve(depth, current_str):
    if depth == k + 1:
        results.append(current_str)
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(int(current_str[-1]), i, signs[depth-1]):
                visited[i] = True
                solve(depth + 1, current_str + str(i))
                visited[i] = False

solve(0, "")

print(results[-1])
print(results[0])