# 알파벳은 출력, 우선 순위 계산하는 함수 만들어서 연산자 우선순위 정하고,  ( -> * -> + 
# 연산자들은 스택에 넣는다. 스택에 아무것도 없으면 push, 스택에 있고, 다음 나오는 연산자보다 우선순위가 높으면 pop. while문으로
spot = {'(': 0, ')': 0, 
        '+': 1, '-' : 1, 
        '*': 2, '/' : 2}

s = input()
stack = []

for i in range(len(s)):

    if s[i] in ['+', '-', '*', '/']:
        while stack and (spot.get(s[i]) <= spot.get(stack[-1])): # 스택이 빌때까지 그리고 스택에 있는 연산자보다 우선순위가 높다면 출력
                print(stack.pop(),end="")
        stack.append(s[i])
    elif s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        top_ch = stack.pop()
        while(top_ch != '('):
            print(top_ch,end="")
            top_ch = stack.pop()
    else:
        print(s[i],end="")
        
while stack:
    print(stack.pop(),end="")