#### 10828. 스택

```python
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

```



#### 15815. 천재 수학자 성필

```python
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

```



#### 4949. 균형잡힌세상

```python
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

```



#### 23253. 자료구조는 정말 최고야

```python
# 23253. 자료구조는 정말 최고야
import sys
N, M = map(int, input().split())  # N : 교과서의 수 , M : 교과서 더미의 수 M

is_valid = 'Yes'
for _ in range(M):
    k = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))[:k]
    if arr != sorted(arr,reverse=True):
        is_valid='No'
        break
print(is_valid)

```



#### 2257. 화학 식량

```python
# 2257. 화학 식량
cemical = { "H" : 1, "C" : 12, "O" : 16 }

from collections import deque
stack = deque()
s = input()
for k in s:
    if k in cemical:
        stack.append(cemical[k])
    elif k == '(':
        stack.append(k)
    elif k == ')':
        tmp = 0
        while True:
            v = stack.pop()
            if v=='(':
                break
            tmp += v
        if tmp ==0:
            continue
        else:
            stack.append(tmp)
    else: # 숫자일 경우
        tmp = stack.pop()
        tmp = tmp*int(k)
        stack.append(tmp)
print(sum(stack))

```



#### 12789. 도키도키 간식드리미

```python
# 12789. 도키도키 간식드리미
from collections import deque
import sys
# [ 입력 ]
N = int(sys.stdin.readline()) # 현재 승환이의 앞에 서 있는 학생들의 수
arr = deque(list(map(int,sys.stdin.readline().split())))
stack = deque()
cnt = 1
while arr:
    if arr and cnt == arr[0]:
        arr.popleft()
        cnt += 1
    else:
        stack.append(arr.popleft())
    while stack and cnt == stack[-1]:
        stack.pop()
        cnt += 1
if stack:
    print('Sad')
else:
    print('Nice')

```



#### 17298. 오큰수

```python
# 17298. 오큰수
import sys
from collections import deque
N = int(sys.stdin.readline())  # 크기가 N인 수열

arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
stack = deque([0])
for i in range(1,N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
print(*result)

```

