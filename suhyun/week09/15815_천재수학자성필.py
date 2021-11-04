# 15815. 천재 수학자 성필
from collections import deque

s = input()
stack = deque()
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        stack.append(int(s[i]))
    else:
        if s[i] == '+':
            rst = (stack.pop() + stack.pop())
        elif s[i] == '-':
            rst1 = stack.pop()
            rst2 = stack.pop()
            rst = rst2 - rst1
        elif s[i] == '*':
            rst = (stack.pop() * stack.pop())
        else:
            rst1 = stack.pop()
            rst2 = stack.pop()
            rst = rst2 // rst1
        stack.append(rst)
print(stack.pop())
