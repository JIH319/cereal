# 제로

```python
import sys
input = sys.stdin.readline

N = int(input())
sequence = [int(input()) for _ in range(N)]
stack = []

for i in sequence:
    if i:stack.append(i) #0아니면 스택에 넣고
    else:stack.pop() #0이면 팝팝

result = 0
for i in stack: 
    result += i #나머지들 더하기

print(result)
```

# 괄호 짝짓기(오류..)

```python
N = int(input())
for tc in range(1, N + 1):
    sequence = input()
    expression = {'[': ']', '{': '}', '(': ')', '<': '>'}
    stack = []

    print('#{}'.format(tc), end=" ")
    for i in sequence:
        if i in expression.keys():
            stack.append(i)
        else:
            if i == expression[stack[-1]]: #하나씩 비교해서 그 쌍만 없애주는 건 알겠는데.. 이렇게 하묜 왜. 아는 사람을 알려조..
                stack.pop()
            else:
                break

    if stack: print(0)
    else: print(1)
```

# 스택수열

```python
import sys
input = sys.stdin.readline

N = int(input())
sequence = [int(input()) for _ in range(N)]

stack = []
expression = []
base = 1  # 기본값 1~N까지니까 처음에 들어오는 수

for i in sequence:
    while base <= i:  # 처음 값보다 작거나 같은 값일때만 작동
        stack.append(base)  # 베이스를 다 스택에 어펜드
        expression.append('+')  # 표현식에 + 추가 
        base += 1  # 비교값은 1개 올라간다
    else:  # 와일이 아닐때 즉 i보다 클때는
        if stack[-1] == i:  # 그 값이 스택에 젤 위에 있으면
            stack.pop()  # 팝을 하고
            expression.append('-')  # 표현식에 -추가

if stack:  # 다 돈다음 스택이 아직도 남아있으면 안되는거다 NO WAYYYYYYY
    print('NO')
else:  # 표현식에 있는거를 하나씩 출력
    for i in expression:
        print(i)
```

# 
