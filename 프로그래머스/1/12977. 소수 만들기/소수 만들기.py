def solution(nums):
    num = sum(nums)

    data = [True] * (num+1)
    data[0]=data[1]=False
    for i in range(2, int(num**0.5)+1):
        for j in range(i*i, num+1, i):
            data[j] = False
    
    n = len(nums)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if data[nums[i]+nums[j]+nums[k]]: cnt += 1

    return cnt