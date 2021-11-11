import sys
stack = []
N = sys.stdin.readline()
for i in range(len(N)):
    # 숫자인 경우, stack에 push
    if '0' <= N[i] <= '9':
        stack.append(int(N[i]))
    # 사칙연산의 경우, 꺼내고 꺼내서 계산하기(순서 조심!!)
    else:
        if N[i] == '+':
            r1 = stack.pop()
            r2 = stack.pop()
            result = r2 + r1
            stack.append(result)
        elif N[i] == '-':
            r1 = stack.pop()
            r2 = stack.pop()
            result = r2 - r1
            stack.append(result)
        elif N[i] == '*':
            r1 = stack.pop()
            r2 = stack.pop()
            result = r2 * r1
            stack.append(result)
        elif N[i] == '/':
            r1 = stack.pop()
            r2 = stack.pop()
            result = r2 / r1
            stack.append(result)

print(int(stack[-1]))
