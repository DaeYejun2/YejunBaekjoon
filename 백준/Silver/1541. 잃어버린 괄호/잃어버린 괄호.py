data = input().split('-')
ans = sum(map(int,data[0].split('+')))
for x in data[1:]:
    x=sum(map(int,x.split('+')))
    ans-=x
print(ans)