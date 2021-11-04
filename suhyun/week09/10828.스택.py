# 10828. 스택
# push X : 정수 X를 스택에 넣는 연산
# pop : 스택에 들어있는 정수가 없는 경우에는 -1
# size : 스택에 들어있는 정수의 개수를 출력한다.
# empty : 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 드러있는 정수가 없는 경우에는 -1을 출력한다.
from collections import deque
import sys
# [ 입력 ]
N = int(sys.stdin.readline())  # 명령의 수
stack = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    else:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
