import sys
input = sys.stdin.readline

N = int(input())
stack = [] # 스택 수열 만들기 위한 스택
result = []
cnt = 1
for _ in range(N):
    M = int(input())
    if not stack or stack[-1] < M:
        for i in range(cnt, M+1):
            stack.append(i)
            result.append('+')
        stack.pop()
        result.append('-')
        cnt = M+1
    elif stack[-1] == M:
        stack.pop()
        result.append('-')
    else:
        break
if stack:
    print('NO')
else:
    print('\n'.join(result))


