# 10828. 스택

```python
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 주어지는 명령의 수 N
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고 100,000보다 작거나 같다.

# for문으로 N번만큼 반복하면서 한번 반복할때마다 input값을 split으로 나눠받아준다.
# 받은 input값을 변수 data 할당하고 data의 첫번째 값이 명령어 이므로 val 변수에 명령어만 따로 할당하여 작성한다.
# 그냥 input을 쓰면 input값이 많아 시간제한 초과가 나니 sys 모듈을 import해서 받아주면 해결된다.


# 시간초과로 인해 sys 활용
import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    data = sys.stdin.readline().split()
    # data의 첫번째 값이 명령어
    val = data[0]

    # 정수 push
    if val == 'push':
        stack.append(int(data[1]))

    # stack이 빈값이면 -1 출력, 아니면 pop한 값을 출력
    elif val == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # 현재 stack의 개수 출력
    elif val == 'size':
        print(len(stack))

    # stack이 비어있으면 1 아니면 0 출력
    elif val == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # stack이 비어있으면 -1 출력 아니면 stack의 마지막값 출력
    elif val == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

```



---

# 15815. 천재수학자성필

```python
# 0~9 숫자와 연산자 + - * / 로만 이루어져 있다.
# 잘못된 수식이 입력되는 경우는 없다.

# 주어진 연산자 목록을 리스트로 만들어 oper 라는 변수에 할당해주고
# input을 받은 data를 하나씩 순회하면서 해당 값이 oper 안에 존재하면 연산자, 아니면 피연산자인 식을 작성한다.
# 연산자일경우 stack의 가장 위의 값이 나중에 작성된 피연산자 이므로 가장 위의 값을 pop하여 b로 그 다음값을 a로 pop 하여 대입한다.
# 나누기 연산자(/)일 경우 3/3일때 1.0이 반환되므로 a//b로 숫자 1이 반환 될 수 있게 몫을 반환하는 식을 작성한다.


# 연산자 리스트 oper
oper = ['+','-','*','/']
data = list(input())

stack = []
for val in data:
    # val이 연산자 라면 stack 상단 2개의 값을 pop
    if val in oper:
        # stack의 최상단 값이 나중에 들어온 값이므로 b,a 로 pop하기
        b = stack.pop()
        a = stack.pop()

        # 연산하여 stack에 다시 push
        if val == '+':
            stack.append(a+b)
        elif val == '-':
            stack.append(a-b)
        elif val == '*':
            stack.append(a*b)
        elif val == '/':
            stack.append(a//b)

    # val이 연산자가 아니라면(피연산자 라면) stack에 push
    else:
        stack.append(int(val))
print(stack[0])

```



---

# 4949. 균형잡힌세상

```python
# 주어진 입력값의 괄호가 균형이 잘 맞춰져 있는지 판단하는게 목적이다.
# 입력값은 한 줄일 수도 있고 여러 줄 일 수도 있다.
# 입력의 종료조건으로 맨 마지막에 점 하나(단 하나 ".")가 들어온다.
# 몇줄인지 N이 안주어지기 때문에 종료조건인 점 하나가 올때까지 반복하여 입력값을 받아야 한다.

# 여는 괄호 리스트인 A와 닫는 괄호 리스트인 B를 만들어두자
# 입력받은 데이터를 한 줄 마다 한요소씩 순회하며 검사하자
# 만약 순회하는 i가 여는 괄호 라면 stack에 push 한다.
# 닫는 괄호 라면 stack의 마지막요소를 pop하여 비교한다.
# pop은 빈값에서 실행하면 오류가 발생하고 빈값인 상태에서 닫는 괄호가 나와도 균형이 맞지 않으니 no를 반환
# 검사가 끝난후에 stack에 여는 괄호가 남아있다면 균형이 맞지않음



# 종료조건 설정을 위해 함수로 작성하였다.
def solve(val):
    stack = []
    for i in val:
        # i가 여는괄호 리스트에 있다면 stack에 push
        if i in A:
            stack.append(i)
        # i가 닫는괄호 리스트에 있고 빈값이 아니라면 pop (빈값이면 균형 맞지 않음 no 출력)
        elif i in B:
            if len(stack) == 0:
                return 'no'
            sp = stack.pop()

            # 닫는 괄호인 i가 여는 괄호인 sp와 균형이 맞지 않으면 no 출력 맞으면 pass
            if i == ')' and sp != '(':
                return 'no'

            elif i == ']' and sp != '[':
                return 'no'
    # 반복문이 끝나고 stack이 빈값이 아니면 균형이 맞지 않는 문장
    if len(stack) > 0:
        return 'no'
    else:
        return 'yes'


data = []
while True:
    input_data = input()
    # 점(.)이 나올때 까지 입력값 받기
    if input_data != '.':
        data.append(input_data)
    else:
        break

A = ['(','[']   # 여는 괄호 리스트
B = [')',']']   # 닫는 괄호 리스트
for val in data:# 입력값을 한줄씩 검사
    result = solve(val)
    print(result)
```



---

# 23253. 자료구조는 정말 최고야

```python
# N : 교과서의 수
# M : 교과서 더미의 수
# 둘째 줄부터 M*2 줄에 걸쳐 입력값 주어짐
# 교과서 더미의 수 만큼 배열을 만들어서 하나의 배열에 합치기(2차원배열)

# 각 더미를 순서대로 순회하는게 아니다!!
# 하나씩 뽑아서 뽑은것들끼리 비교, 가장 작은값을 result 배열에 넣자
# 그 다음은 result의 마지막요소와 비교해서 result가 더 크다면 No

# 구현을 못했다...
# 시간이 남는다면 위의 아이디어로 다시 풀어보자

# 질문검색을 참고해서 내림차순으로 정렬하면 된다는 아이디어를 얻고 풀어보았다.
# 입력값을 받고 정렬하여 검사하면 시간초과
# sys 모듈을 쓰지 않으면 시간초과
# 입력을 받고나서 바로 검사하여 확인해야한다.

import sys

N,M = map(int,sys.stdin.readline().split())
for i in range(M):
    _ = sys.stdin.readline() # 책의 개수는 필요없기에 변수에 할당하지 않는다.
    book = list(map(int,sys.stdin.readline().split()))
    # 내림차순값을 sort_data 에 할당하고 원본과 비교
    sort_data = sorted(book,reverse=True)
    if book != sort_data:
        print('No')
        break
else:
    print('Yes')

```



---

# 2257. 화학식량

```python
# H : 수소, 질량 1
# C : 탄소, 질량 12
# O : 산소, 질량 16

# 입력값을 숫자로 변환하여 stack에 넣고
# 입력값이 숫자라면 stack의 마지막요소랑 곱하기
# 입력값이 닫는 괄호라면 여는 괄호가 나올때까지 숫자를 꺼내서 더해주기

data = list(input())
stack =[]

for i in data:
    if i == 'H':
        stack.append(1)
    elif i =='C':
        stack.append(12)
    elif i =='O':
        stack.append(16)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        # 여는 괄호가 나올때까지 더한다.
        sum_val = 0
        while True:
            if stack[-1] != '(':
                pop_data = stack.pop()
                sum_val += pop_data
            # 여는 괄호가 나온다면 여는 괄호 pop해서 빼주고 계속 더한값 sum_val을 push 한다.
            else:
                stack.pop()
                stack.append(sum_val)
                break
    else:
        pop_data = stack.pop()
        stack.append(pop_data*int(i))

print(sum(stack))
```



---

# 12789. 도키도키 간식드리미

```python
```



---

# 17298. 오큰수

```python
```

