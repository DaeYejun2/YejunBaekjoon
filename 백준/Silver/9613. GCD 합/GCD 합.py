import sys
import math
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    command = []
    command = list(map(int, sys.stdin.readline().rstrip().split()))
    sum = 0
    for i in range(command[0]):
        tmp = i+2
        while(tmp <= command[0]):
            sum += math.gcd(command[i+1],command[tmp])
            tmp+=1
    print(sum)