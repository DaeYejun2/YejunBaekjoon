def solution(arr1, arr2):
    res = [[0] * len(arr1[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            res[i][j] = arr1[i][j] + arr2[i][j]
    return res