import sys
input = sys.stdin.readline

n = int(input())
n_data = [];p_data = []; ans = 0

for _ in range(n):
    a=int(input())
    if a <= 0: n_data.append(a)
    else: p_data.append(a)

n_data.sort()
n_data += [1]
if len(n_data) >= 2:
    for i in range(0, len(n_data), 2):
        if len(n_data) % 2:
            if n_data[i] == 1:
                break
        else:
            if n_data[i+1] == 1:
                ans += n_data[i]; break
            
        ans+= max(n_data[i]*n_data[i+1], n_data[i]+n_data[i+1])

p_data.sort(reverse=True)
p_data += [0]
if len(p_data) >= 2:
    for i in range(0, len(p_data), 2):
        if len(p_data) % 2:
            if p_data[i] == 0:
                break
        else:
            if p_data[i+1] == 0:
                ans += p_data[i]; break
        ans += max(p_data[i]*p_data[i+1], p_data[i]+p_data[i+1])

        
print(ans)