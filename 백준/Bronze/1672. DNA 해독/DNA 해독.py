import sys
input = sys.stdin.readline

n = int(input())
idx = n-2
le = list(input().rstrip())
cnt = 0

data = {
    "AA": "A", "AG": "C", "AC": "A", "AT": "G",
    "GA": "C", "GG": "G", "GC": "T", "GT": "A",
    "CA": "A", "CG": "T", "CC": "C", "CT": "G",
    "TA": "G", "TG": "A", "TC": "G", "TT": "T"
}

while True:
    if len(le) == 1: break
    tmp = le[idx]+le[idx+1]
    le.pop()
    le[idx] = data[tmp]
    idx -= 1
    cnt += 1
    
print(le[0])