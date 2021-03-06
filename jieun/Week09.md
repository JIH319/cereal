# 10828. 스택
```python
import sys
input = sys.stdin.readline
stack = []

for _ in range(int(input())):
    data = input().split()
    # push면 stack에 추가
    if data[0] == 'push':
        stack.append(data[1])
    # stack이 존재하면 top 출력 아니면 -1
    elif data[0] == 'top':
        print(stack[-1] if stack else -1)
    # stack 길이 출력
    elif data[0] == 'size':
        print(len(stack))
    # 스택이 있으면 0 아니면 1
    elif data[0] == 'empty':
        print(0 if stack else 1)
    # 스택이 있으면 pop 아니면 -1
    elif data[0] == 'pop':
        print(stack.pop() if stack else -1)
```


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

# 4949. 균형잡힌 세상
```python
import sys
input = sys.stdin.readline

while True:
    words = input().rstrip()
    if words == '.':
        break
    stack = []
    isBal = True

    for word in words:
        if word == '(' or word == '[':
            stack.append(word)

        elif word == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else :
                isBal = False
                break

        elif word == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else :
                isBal = False
                break

    if isBal and not stack:
        print('yes')
    else:
        print('no')
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

# 12789. 도키도키 간식드리미
```python
N = int(input())
num = 1
# 원래 줄
stack = list(map(int, input().split()))[::-1]
# 한명씩 설 수 있는 공간
new_stack = []

while stack or new_stack:
    # 만약 한명씩 설 수 있는 공간에 사람이 있고, 맨 앞 사람이 지금 나와야하는 num과 같으면 pop, num ++
    if new_stack and new_stack[-1] == num:
        new_stack.pop()
        num += 1
        continue
    # 한 명씩 설수 있는 공간에 아무도 없거나 맨 앞사람이 지금 나와야하는 번호가 아니면 줄 서 있는 곳에서 일단 한명 pop
    student = stack.pop()
    # 만약 지금 pop한 애가 맞는 순서라면
    if student == num:
        num += 1
        continue
    # 만약 한명씩 설 수 있는 공간에 사람이 있고, 그 사람의 순서보다 지금 pop한 애 순서가 더 클 경우 무조건 sad
    if new_stack and new_stack[-1] < student:
        print('Sad')
        break
    # 그게 아니라면 일단 한명씩 줄서는 공간에 student 추가
    new_stack.append(student)
else:
    # break 걸리지 않고 while문 끝나면 nice 출력
    print('Nice')
```


# 17298. 오큰수
```python
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# 오큰수 초기화
NGE = [-1]*N
stack = deque()
# A 배열 앞에서부터 차례로 돌면서 확인
for i in range(N):
    # stack이 있고 stack top의 첫번째값(수열 A[i-k]의 값)이 A[i]보다 작을 경우, pop 해주면서 오큰수 업데이트
    while stack and (stack[-1][0] < A[i]):
        tmp, idx = stack.pop()
        NGE[idx] = A[i]
    # stack이 없거나, stack top의 첫번째 값이 A[i]보다 클 경우 stack에 추가
    stack.append([A[i], i])

print(*NGE)
```
