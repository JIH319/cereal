import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break

    stack = []
    result = 'yes'
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
                break

        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
                break

    if stack or result == 'no':
        result = 'no'
    print(result)