def solution(survey, c):
    data = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i, s in enumerate(survey):
        if c[i] == 4: continue
        if c[i] > 4:
            data[s[1]] += c[i]-4
        else:
            data[s[0]] += 4-c[i]
    res = ''

    item = list(data.items())
    le = len(item)

    for i in range(0, le-1, 2):
        if item[i][1] >= item[i+1][1]:
            res += item[i][0]
        else: res += item[i+1][0]
    return (res)