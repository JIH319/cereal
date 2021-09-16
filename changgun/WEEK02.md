#### [백준/10773] 제로

```python
N = int(input())
stack = []
for _ in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
```



#### [SWEA/1218]  괄호 짝짓기

```python
for tc in range(1, 10+1):
    N = int(input())
    test = list(input())
    stack = []
    result = 1
    for i in range(N):
        if test[i] in ['(', '{', '[', '<']:
            stack.append(test[i])
        elif test[i] == ')':
            if stack.pop() == '(':
                continue
            else:
                result = 0
                break
        elif test[i] == '}':
            if stack.pop() == '{':
                continue
            else:
                result = 0
                break
        elif test[i] == ']':
            if stack.pop() == '[':
                continue
            else:
                result = 0
                break
        elif test[i] == '>':
            if stack.pop() == '<':
                continue
            else:
                result = 0
                break
    if stack:
        result = 0
    print('#{} {}'.format(tc, result))
```



#### [백준/1874/스택 수열]

```python
n = int(input())
stack = []
result = []
count = 0
valid = True

for _ in range(n):
    target = int(input())
    while count < target:
        count += 1
        stack.append(count)
        result.append('+')
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        valid = False
        break
if not valid:
    print('No')
else:
    for i in result:
        print(i)
```

