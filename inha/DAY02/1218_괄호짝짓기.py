for tc in range(1, 11):
    N = int(input())
    bracket = list(input())
    stack = []
    result = 1
    for i in range(N):
        if bracket[i] == '(' or bracket[i] == '{' or bracket[i] == '[' or bracket[i] == '<':
            stack.append(bracket[i])
        elif bracket[i] == ')':
            if stack.pop() == '(':
                continue
            else:
                result = 0
                break
        elif bracket[i] == '}':
            if stack.pop() == '{':
                continue
            else:
                result = 0
                break
        elif bracket[i] == ']':
            if stack.pop() == '[':
                continue
            else:
                result = 0
                break
        elif bracket[i] == '>':
            if stack.pop() == '<':
                continue
            else:
                result = 0
                break
    if stack:
        result = 0
    print('#{} {}'.format(tc, result))
