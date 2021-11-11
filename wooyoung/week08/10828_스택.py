import sys
N = int(sys.stdin.readline()) # 명령의 갯수
stack = []
for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        stack.append(word[1])

    elif order == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
