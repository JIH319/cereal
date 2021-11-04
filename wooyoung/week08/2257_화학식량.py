import sys
from collections import deque
arr = list(sys.stdin.readline())
my_dict = {'O': 16,
           'C': 12,
           'H': 1}
stack = deque()

for i in arr:
    if i in ('O', 'C', 'H'):
        stack.append(my_dict.get(i))

    elif i == '(':
        stack.append(i)

    # 닫는괄호는 여는 괄호와 짝꿍!
    elif i == ')':
        # 여는 괄호가 나올때까지 stack의 숫자들을 더하고
        # 여는 괄호는 pop
        # 더한 숫자 다시 push
        sum_v = 0
        while True:
            if stack[-1] == '(':
                stack.pop()
                stack.append(sum_v)
                break

            sum_v += stack.pop()
    # 숫자가 나오는 경우 곱해줘야 한다.
    elif '1' <= i <= '9':
        a_num = stack.pop()
        stack.append(a_num * int(i))

print(sum(stack))