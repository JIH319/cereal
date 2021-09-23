##  10773. 제로 

```python
# 10773 제로!
# 나코더 기장 재민이는 동아리 회식을 준비하기 위해 장부를 관리하는 중.
# 재현이는 재민이를 돕는다. 재현이는 돈을 시수로 잘못 부르는 사고를 치기 일수.
# 재현이는 잘못된 수를 부를 떄 마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지운다.

# 스택을 활용하자!
from collections import deque
stack = deque()
# [ 입력 ]
# 첫 번째 줄에 정수 K 가 주어진다.
K = int(input())
# 스택
# 이후 K개의 줄에 정수 1개씩 주어진다.
for _ in range(K):
    n = int(input())
    # n 이 존재할경우 stack 에 append 해준다.
    if n:
        stack.append(n)
    # 존재하지 않을경우, 가장 최근에 들어간 수를 pop 해준다.
    else:
        stack.pop()
# 최종적으로 나온 stack 에 sum 을 활용한다.
print(sum(stack))

```



###  1218. [S/W 문제해결 기본] 4일차 괄호 짝짓기

```python
# 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기

# 4 종류의 괄호 문자들 '()','[]','{}','<>'로 이루어진 문자열ㅇ 주어진다.
# 괄호의 짝이 모두 맞는지 판별하는 프로그램을 작성한다

# deque 를 활용하자
from collections import deque


# 테스트 케이스가 유효한지 안유호한지 확인할 confirm 함수 생성
def confirm(t, n):
    # 값을 받을 que 생성
    stack = deque()
    # 테스트 케이스 줄 길이 만큼 반복문 생성
    for i in range(n):
        # 여는 괄호일경우 바로 append 해준다.
        if t[i] == '{' or t[i] == '[' or t[i] == '(' or t[i] == '<':
            stack.append(t[i])
        # 닫는 괄호일겨우, 스택에 저장된 마지막 값이 매칭 될 경우, continue 로 올려주고,
        # 안될 경우 return 0 을 바로 반환한다.
        elif t[i] == ')':
            if stack.pop() == '(':
                continue
            else:
                return 0
        elif t[i] == '}':
            if stack.pop() == '{':
                continue
            else:
                return 0
        elif t[i] == ']':
            if stack.pop() == '[':
                continue
            else:
                return 0
        elif t[i] == '>':
            if stack.pop() == '<':
                continue
            else:
                return 0
    # 반복문이 끝나도록 반환이 되지 않을 경우, 모두 매칭이 된 경우 1을 반환한다.
    return 1


# [ 입력 ]
T = 10
for tc in range(1, T + 1):
    # 각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 길이가 주어진다.
    N = int(input())
    # 괄호 짝짓기 테스트 케이스가 주어진다.
    test = input()
    # 결과 값 1 과 0을 반활 받을 result 변수 생성
    result = confirm(test, N)
    # 결과 값 출력
    print('#{} {}'.format(tc, result))

```



### 1874. 스택 수열

```python
# 스택 수열
# 스택은 LIFO 구조

# deque 를 활용하자!
from collections import deque
import sys
input = sys.stdin.readline


# [입력]
# 첫 줄에 n 이 주어진다.
N = int(input())
# 둘째 줄부터 n개의 줄에는 수열을 이루는 1 이상 n 이하의 정수가 하나씩 순서대로 주어진다.
stack = deque()
x0 = 1
rst = []
for _ in range(N):
    K = int(input())
    # stack 이 없거나, 또는 stack 의 마지막 값이  입력값 K보다 작은경우, 값을 받앚운다.
    if not stack or stack[-1] < K:
        for i in range(x0,N+1):
            # K 와 일치하지 않으면, stack 에 push 해주고, rst 에 + 추가
            if i != K:
                stack.append(i)
                rst.append('+')
            # 일치할 경우, stack 에 넣지 않고 rst 에 +, -  추가
            else:
                rst.extend(['+','-'])
                x0 = i+1
                break
    # stack 에 맨 오른쪽 값이 입력값 K 와 일치할 경우, pop 해주고 rst 에 - 추가
    elif stack[-1] == K:
        stack.pop()
        rst.append('-')
    # 이 모든 경우에 해당하지 않을 경우, 만들고자 하는 수열을 제작할 수 없는 것이다. break 한다.
    else:
        break
# 이 과정에서 stack 이 남은경우, 수열을 만들다 남은경우 No를 출력
if stack:
    print('NO')
# stack 을 모두 소비하여 결과물이 나온 경우, 해당 리스트를 개행하여 출력해준다.
else:
    for r in rst:
        print(r)

```

