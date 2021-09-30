### [백준/10773] 제로

```python
import sys
input = sys.stdin.readline

N = int(input())
money = []
for _ in range(N):
    M = int(input())
    if M:
        money.append(M)
    else:
        money.pop()

result = sum(money)
print(result)
```



### [SWEA/1218] 괄호 짝짓기

```python
import sys

sys.stdin = open('1218_input.txt')

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
```



### [백준/1874] 스택 수열

```python
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
```

