# 4949. 균형잡힌 세상
from collections import deque

while True:
    s = input()
    stack = deque()
    is_valid = 'yes'
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_valid = 'no'
                break
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_valid = 'no'
                break
    if stack:
        is_valid = 'no'
    if s == '.':
        break
    print(is_valid)
