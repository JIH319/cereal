# 1874. 스택수열

```python
N = int(input())
arr = [int(input()) for _ in range(N)] # N만큼 input값 받아서 list에 넣기
i = 0
stack = []
result = []
for val in range(1,N+1): # 1부터 N까지 한개씩
    stack.append(val) # push
    result.append('+')  # push하면 result에 +를 push
    # 마지막에 stack이 다 빈상태로 while을 한번더 검사하는데 빈상태에서 [-1]을 해버려서 인덱스 에러가 난다.
    # stack에 값이 존재할때 검사하라는 조건을 넣어서 인덱스 에러를 피해준다.
    while stack and stack[-1] == arr[i]: # 반복문 검사
        stack.pop() # stack에 값이 있고 stack 마지막인덱스가 arr의 i번째 인덱스와 같은값이면 pop
        result.append('-') # pop 할때마다 -를 result에 push
        i += 1
if stack:
    print('NO') # 반복문이 끝나고 stack에 남은 값이 있다면 NO
else:
    for x in result: # stack이 다 비었다면 result에 있는 값을 출력
        print(x)


```



# 10773. 제로

```python
K = int(input())
stack = []
for _ in range(K):
    N = int(input())
    if N == 0:
        stack.pop() # N이 0이면 pop
    else:
        stack.append(N) # 0이 아니면 push
if not stack:   # 다 끝난후에 stack이 비었으면 0
    print(0)
else:
    print(sum(stack))   # 남아있으면 합해서 출력

```



# 1218. 괄호짝짓기

```python
for tc in range(1,11):
    N = int(input())
    input_val = input()
    stack = []
    left = ['(','[','{','<']    # 왼쪽 괄호 리스트
    right = [')',']','}','>']   # 오른쪽 괄호 리스트
    result = 1  # 결과값 1로 미리 지정
    for val in input_val:   # input 값을 for반복으로 하나씩 검사
        if val in left:     # left 안에 있다면 stack 에 push
            stack.append(val)
        elif val in right:  # right 안에 있다면
            if right.index(val) == left.index(stack[-1]):   # val이 stack의 마지막값과 짝이 맞는지 검사
                stack.pop() # 맞으면 스택의 마지막 값 pop 하고 val은 아무런 지정을 안해줌
            else:
                result = 0  # 안맞으면 유효하지 않은 값이라 0으로 지정하고 반복문 종료
                break
    
    print('#{} {}'.format(tc,result))
```





