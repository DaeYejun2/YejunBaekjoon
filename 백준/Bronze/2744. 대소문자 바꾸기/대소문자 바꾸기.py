for s in input():
    if ord("A") <= ord(s) <= ord("Z"):
        print(s.lower(),end='')
    else:
        print(s.upper(),end='')