## 1) 백준_1073.제로

```python
# 풀이 방법 : stack 

stack = []
#K만큼 반복해서 변수 받기
K = int(input())
for k in range(K):
    a = int(input())
    # 변수가 0이 아닌 경우,
    if a:
        stack.append(a)
    # 변수가 0인 경우
    else:
        stack.pop(-1)

print(sum(stack))
```



## 2) swea_1218. 괄호 짝짓기

```python
# 풀이방법 : stack, dict 

for tc in range(1, 11):
    stack = []
    N = int(input())
    S = input()
    # 괄호끼리 dict 만들어주기
    my_dict = {')': '(', ']': '[', '}': '{', '>': '<'}
    result = 1
    # 여는괄호 stack.append, 닫는 괄호 나오면 stack.pop()하고 dict로 비교 
    for i in range(N):
        if S[i] in ('(', '[', '{', '<'):
            stack.append(S[i])
        else:
            a = stack.pop()
            if a != my_dict.get(S[i]):
                result = 0
                break

    print('#{} {}'.format(tc, result))
```



## 3) 백준_1784.스택 수열

```python
# 풀이 방법 1: stack, list 사용
N = int(input())
my_list = []
A = []

for i in range(N):
    A.append(int(input()))

# 리스트에 1부터 n까지 숫자 채우기
for k in range(1, N+1):
    my_list.append(k)

def my_fx(A, my_list):
    stack = []
    result = []
    for a in range(len(A)):
        rabbit = A.pop(0) 

        while my_list and my_list[0] <= rabbit:
            stack.append(my_list.pop(0))
            result += '+'

        if stack[-1] == rabbit:
            stack.pop()
            result += '-'

        else:
            return 'NO'
    return result

wow = my_fx(A, my_list)
if wow == 'NO':
    print('NO')
else:
    for q in wow:
        print(q)


# 풀이 방법 2: stack, +1 사용 , 이게 더 깔끔하다 
N = int(input())

def my_fx():
    stack = []
    result = []
    num = 1

    # N번만큼 target 확인하기
    for r in range(N):
        target = int(input())

        # 스택에 num이 담기도록 하기
        # target이 될 때까지 stack.push
        while num <= target:
            stack.append(num)
            result += '+'
            num += 1

        # stack.pop()
        if stack[-1] == target:
            stack.pop()
            result += '-'

        else:
            return 'NO'

    return result

wow = my_fx()
if wow == 'NO':
    print('NO')
else:
    for q in wow:
        print(q)
```

