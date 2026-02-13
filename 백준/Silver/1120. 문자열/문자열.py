a, b = input().split()
lea=len(a); leb=len(b)
l = leb-lea
cnt = 0

if lea == leb:
    for i in range(lea):
        if a[i] != b[i]:
            cnt += 1
else:
    for i in range(leb):
        tmp = b[i:i+lea]
        t = 0
        for j in range(lea):
            if len(tmp) < lea: break
            if a[j] == tmp[j]:
                t += 1
        cnt = max(cnt, t)

    cnt = lea-cnt
    
print(cnt)