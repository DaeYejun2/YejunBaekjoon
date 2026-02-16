def solution(paper):
    x = []
    y = []

    for r in range(len(paper)):
        for c in range(len(paper[0])):
            if paper[r][c] == '#':
                x.append(r)
                y.append(c)

    return [min(x), min(y), max(x)+1, max(y)+1]