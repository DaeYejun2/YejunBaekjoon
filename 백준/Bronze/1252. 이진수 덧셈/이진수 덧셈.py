a, b = map(str, input().split())
ans = int(a, 2)+int(b, 2)
print(bin(int(ans))[2:])