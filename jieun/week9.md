# 15815. 천재 수학자 성필
```python
data = list(input())
num_stack = []
op_stack = []
# 괄호 안의 연산자를 괄호밖으로 꺼내므로 먼저 계산해야 할 피연산자들 바로 뒤에 연산자가 위치함
# 연산자를 만날때마다 피연산자 두개 꺼내서 계산 후 다시 스택에 집어 넣음
for d in data:
    if d.isdecimal():
        num_stack.append(int(d))
    else:
        b, a = num_stack.pop(), num_stack.pop()
        if d == '+':
            num_stack.append(a+b)
        elif d == '-':
            num_stack.append(a-b)
        elif d == '*':
            num_stack.append(a*b)
        elif d == '/':
            num_stack.append(a//b)

print(num_stack[0])
```

# 23253. 자료구조는 정말 최고야

```python
N, M = map(int, input().split())

for i in range(M):
    k = int(input())
    dummy = list(map(int, input().split()))
    # 그냥 현재 스택에 들어있는 값이 내림차순이 맞는지만 확인하면 된다.
    # 내림차순으로 들어있다면 무조건 순서대로 책을 꺼낼 수 있음
    if sorted(dummy, reverse=True) == dummy:
        continue
    else:
        print('No')
        break
else:
    print('Yes')

```
