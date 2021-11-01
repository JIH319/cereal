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

# 2257. 화학식량
```python
chemi = {'H': 1, 'C': 12, 'O': 16}
data = input()
idx = 0
stack = []

# 덧셈 + 괄호 있는 계산기 로직과 비슷함
while idx < len(data):
    # 여는 괄호일 경우 일단 stack에 집어 넣음
    if data[idx] == '(':
        stack.append('(')
    # 닫는 괄호일 경우
    elif data[idx] == ')':
        # 여는 괄호가 나올 때 까지 pop 해주며 temp_sum에 저장
        temp_sum = 0
        while True:
            temp = stack.pop()
            if temp == '(':
                stack.append(temp_sum)
                break
            temp_sum += temp
        # 만약 여는 괄호 뒤에 숫자가 있으면 stack top에 저장된 괄호 안의 연산 값에 곱하기
        if idx + 1 < len(data) and data[idx+1].isdecimal():
            idx += 1
            stack.append(stack.pop()*int(data[idx]))
    # 만약 숫자일 경우 바로 앞에 있는 원소에 곱해줌
    elif data[idx].isdecimal():
        stack.append(stack.pop()*int(data[idx]))
    # 원소일 경우 숫자로 바꿔줌
    else:
        stack.append(chemi[data[idx]])
    idx += 1

print(sum(stack))
```
