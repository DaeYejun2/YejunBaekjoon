import sys
input = sys.stdin.readline

ml, mr, tl, tr = map(lambda x: "SPR".find(x), input().rstrip().split())
#S, P, R 중 입력을 받으면 "SPR"에서 해당하는 인덱스를 받는다

def lose_case(x):    #지는 case
    return (x+2)%3

if ml==mr and lose_case(ml) in [tl, tr]:
    print("TK")
elif tl==tr and lose_case(tl) in [ml, mr]:
    print("MS")
else:
    print("?")