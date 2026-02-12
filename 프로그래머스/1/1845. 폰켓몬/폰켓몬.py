def solution(nums):
    n = len(nums)
    l = n//2
    nums = set(nums)
    if len(nums)>l: return l
    else: return len(nums)