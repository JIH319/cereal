### 15815_bkj_천재수학자성필

```python
#  연산자가 피연산자 뒤에 위치
# 후순위계산식 결과값 찾기

data = input()
N = len(data)
# 계산과정에서 피연산자를 담을 스택
stack = [0] * N
top = -1
for i in range(N):
    # 피연산자면
    if '0' <= data[i] <= '9':
        top += 1
        stack[top] = int(data[i])
    # 연산자면 >> 계산수행 >> 결과 다시 스택에
    else:
        val2 = stack[top]
        top -= 1
        val1 = stack[top]

        if data[i] == '+':
            stack[top] = val1 + val2
        elif data[i] == '-':
            stack[top] = val1 - val2
        elif data[i] == '*':
            stack[top] = val1 * val2
        elif data[i] == '/':
            stack[top] = val1 / val2
print(int(stack[0]))

```





### 4949_bkj_균형잡힌 세상

```python
open = {'(','['}
close = {')',']'}
# 괄호들의 균형이 잘 맞춰져 있는지 판단
while True:
    data = input()
    # 점 하나만 입력들어오면 >> 입력 종료
    if data == '.':
        break
    
    N = len(data)
    # 여는 괄호를 담을 스택
    stack = []
    result = 1 # 1이면 균형잡힌 괄호 >> YES! 0이면 NO! 출력
    for i in range(N):
        # 여는 괄호면,
        if data[i] in open:
            stack.append(data[i])
        # 닫는 괄호면,
        elif data[i] in close:
            # 스택안에 뽑을게 있다면 >> 진행, 그렇지 않다면 반복종료 >> no
            if stack:
                tmp = stack.pop()
                # 괄호쌍 비교 >> 쌍이 맞다면 다음 비교로 이동
                if data[i] == ')' and tmp == '(':
                    continue
                elif data[i] == ']'and tmp == '[':
                    continue
                # 비교결과 쌍이 맞지 않는다 >> 반복종료 >> no
                result = 0
                break
            else:
                result = 0
                break
    # 스택에 여는 괄호가 남아있다면 >> 균형 X >> no
    if stack:
        result = 0
    if result:
        print('yes')
    else:
        print('no')
```



### 12789_bkj_도키도키 간식드리미

```python
import sys
from collections import deque

N = int(sys.stdin.readline())
data = deque(map(int,sys.stdin.readline().split()))

stack = deque() # 대기열 LIFO
num = 1 # 현재 찾는 번호 (1부터 N까지 순서대로)
idx = 0 # 줄 인덱스
is_break = 0
result = 'Nice'
while True:
    # 줄 선 사람 다 대기줄로 뺐고
    if idx == N:
        # 대기줄 마지막들어간 사람이 찾는 번호 아니면 >>  불가능
        while stack:
            if stack[-1] == num:
                stack.pop()
                num += 1
            else:
                result = 'Sad'
                break
        # 줄선사람, 대기줄 모두 없음 >> while문 탈출
        break 
        
    # 아직 줄 선 사람 남아있음
    else:
        # 줄 선 곳에 찾는 번호 있음
        if data[idx] == num:
            idx += 1
            num += 1
        else:
            # 대기줄에 찾는 번호 있음
            if stack and stack[-1] == num:
                stack.pop()
                num += 1
            # 대기줄에도 찾는 번호 없음 >> 줄 선 사람 대기줄로 옮기기
            else:
                stack.append(data[idx])
                idx += 1

print(result)
```





### 2257_bkj_화학식량

```python
# 화학식은 H, C, O, (, ), 2, 3, 4, 5, 6, 7, 8, 9만으로 이루어진 문자열
# H : 1, C : 12, O : 16
HCO = {'H':1,'C':12,'O':16}
HCO_keys = {'H','C','O'}

data = input()
N = len(data)

idx = 0
stack = []
while idx < N: 
    # 화학원자
    if data[idx] in HCO_keys:
        stack.append(HCO[data[idx]]) 
    # 여는 괄호
    elif data[idx] == '(':
        stack.append(data[idx])
        pass
    # 닫는 괄호
    elif data[idx] == ')':
        tmp = 0
        # 여는 괄호 나올때까지 더해서 stack에 담아주기
        while stack[-1] != '(':
            tmp += stack.pop()
        stack.pop() # 여는 괄호 빼기
        stack.append(tmp) # 방금 괄호쌍 안의 합 넣어주기
        tmp = 0

    # 숫자 >> 직전값 * 숫자
    elif '2' <= data[idx] <= '9':
        stack[-1] = stack[-1] * int(data[idx])

    idx += 1

print(sum(stack))
```

