### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" width="20" height="20">[[10828]스택](https://www.acmicpc.net/problem/10828)

```python
import sys
input = sys.stdin.readline


# Stack 클래스를 만들어서 클래스의 메서드를 만들어주었다.
class Stack:
    # Stack 클래스를 생성하면 빈 리스트가 생성됨
    def __init__(self):
        self.arr = []

    # value 값을 리스트에 삽입
    def push(self, value):
        self.arr.append(value)

    # stack의 마지막 요소 꺼내기
    def pop(self):
        if self.arr:
            return self.arr.pop()
        else:
            return -1

    # stack의 크기 구하기
    def size(self):
        return len(self.arr)
    
    # stack이 비어있는지 확인
    def empty(self):
        if self.arr:
            return 0
        else:
            return 1
    
    # stack 제일 위에 있는 요소 값 찾기
    def top(self):
        if self.arr:
            return self.arr[-1]
        else:
            return -1


N = int(input())
stack = Stack()

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" width="20" height="20">[[15815]천재 수학자 성필](https://www.acmicpc.net/problem/15815)

```python
import sys
input = sys.stdin.readline().rstrip


# 후위표기법
# 연산자는 +, -, *, /
# 0 으로 나누는 경우, 잘못된 수식이 들어오는 경우는 없음, 계산 중간 값은 모두 정수
# 숫자가 나오면 stack에 push,
# 연산자가 나오면 stack 안의 숫자들 빼서 계산
def postfix(exp):
    stack = []
    for op in exp:
        if op == '+':
            stack.append(stack.pop()+stack.pop())
        elif op == '-':
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(val1-val2)
        elif op == '*':
            stack.append(stack.pop()*stack.pop())
        elif op == '/':
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(int(val1/val2))
        else:
            stack.append(op)
    return stack[-1]


exp = list(input())
for i in range(len(exp)):
    # 숫자면 int 타입으로 다시 저장
    if exp[i].isdigit():
        exp[i] = int(exp[i])
print(postfix(exp))
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" width="20" height="20">[[4949]균형잡힌 세상](https://www.acmicpc.net/problem/4949)

```python
import sys
input = sys.stdin.readline

# 괄호검사
# 아무 괄호도 오지 않고 종료(.)될 경우에도 'yes' 출력
# 들어오는 입력을 모두 처리하기 위해 while True
while True:
    sentence = input().rstrip()
    # 입력 종료 조건으로 맨 마지막에 . 이 들어오므로
    # 종료 조건
    if sentence == '.':
        break
    # 열린 괄호를 저장할 stack 생성
    stack = []
    # 괄호가 짝을 이루는지 알려주는 isTrue 변수
    # 짝을 이루면 True, 안 이루면 False
    isTrue = True
    for c in sentence:
        # 열린 괄호가 오면 stack에 넣고
        if c == '(' or c == '[':
            stack.append(c)
        # 닫힌 괄호가 오면 stack에서 pop한 값과 비교하기
        elif c == ')':
            # 닫힌 괄호가 왔을 때 stack이 비어있거나
            # 열린 괄호에 맞는 닫힌 괄호가 아닐 경우
            # 짝이 맞지 않으므로 isTrue 변수에 False를 저장하고 break
            if not stack or stack.pop() != '(':
                isTrue = False
                break
        elif c == ']':
            if not stack or stack.pop() != '[':
                isTrue = False
                break
    # 괄호의 짝이 맞으면 stack 안에 있는 괄호는 모두 pop 되어야함
    # 괄호의 짝이 맞지 않는 경우
    # 1. stack에 남아있다는 것은 괄호 짝이 맞지 않음을 의미
    # 2. stack이 비어있어도 isTrue가 False인 경우는 짝이 맞지 않음
    if stack or not isTrue:
        print('no')
    else:
        print('yes')
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/6.svg" width="20" height="20">[[23253]자료구조는 정말 최고야](https://www.acmicpc.net/problem/23253)

```python
import sys
input = sys.stdin.readline

# 책 개수 N개, 책 더미 M개
N, M = map(int, input().split())
# 책을 순번대로 정리 가능한지 나타내는 변수 isTrue
# 가능하면 True, 불가능하면 False
isTrue = True
# 책 더미가 M개 이므로 M번 체크
# 책을 순번대로 정리할 수 있으려면 각 더미에 쌓여있는 책들의
# 순번이 높은 책이 위에 있어야함
for i in range(M):
    # 순서대로 쌓는거 불가능하면 M개의 더미를 다 확인할 필요 X
    if not isTrue:
        break
    # 각 더미의 책들을 쌓을 stack
    stack = []
    # 각 더미의 책 개수
    book_cnt = int(input())
    # 각 더미의 책 순번
    books = list(map(int, input().split()))
    for book in books:
        # 순번이 더 큰 책이 위에 오면 순번대로 책 정리 불가
        if stack and stack[-1] < book:
            isTrue = False
            break
        else:
            stack.append(book)
# 결과 출력
if isTrue:
    print('Yes')
else:
    print('No')
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" width="20" height="20">[[2257]화학식량](https://www.acmicpc.net/problem/2257)

```python
# 음.. 이 방법은 stack이 아닌 것 같긴 한데..
import sys
input = sys.stdin.readline

chemical = list(input().rstrip())

# 각 원자의 질량
dic_vol = {'H': 1, 'C': 12, 'O': 16}
# 원자는 9개까지 가능
nums = {'2', '3', '4', '5', '6', '7', '8', '9'}
N = len(chemical)

# 괄호 안의 값들끼리 계산하기 위해서
# 괄호의 계산값은 각 인덱스에 저장됨
# H(CO) 일 경우 lst[0] = 1(H),
# lst[1] = 28(CO) 가 저장되도록
lst = [0]*N

# idx: 화학식을 입력받은 chemical 리스트에 접근하기 위한 인덱스 변수
# i: 합계를 저장할 lst의 인덱스 변수
# val_cur: 계산 중간에 원자 개수와 원자량을 계산하기 위한 현재 값 변수
idx, i, cur_val = 0, 0, 0
# 입력받은 리트스를 끝까지 돈다.
while idx < N:
    # chemical[idx]가 원자이면(H, C, O)
    # 현재 값 cur_val 변수에 원자량 저장하고
    # lst[i]에 해당 원자량 값을 더한다.
    if chemical[idx] == 'H' or chemical[idx] == 'C' or chemical[idx] == 'O':
        cur_val = dic_vol[chemical[idx]]
        lst[i] += dic_vol[chemical[idx]]
    # chemical[idx]값이 nums안에 들어있는 숫자라면
    # 원자 다음에 숫자가 올 것이므로 앞에서 lst[i]에 해당 원자량만큼 더해준 것을 빼주고
    # 해당 원자량(cur_val)과 현재 idx가 가르키는 숫자를 곱한 값을 다시 더해준다.
    elif chemical[idx] in nums:
        lst[i] -= cur_val
        lst[i] += cur_val * int(chemical[idx])
    # 열린 괄호가 오면 괄호 안의 값은 따로 계산되어야 하므로
    # lst의 인덱스인 i를 +1 증가시켜 lst[i+1]에서 새로오는 괄호 안의 값들을 계산하여 저장하도록 함
    elif chemical[idx] == '(':
        i += 1
    # 닫힌 괄호가 오면 현재 괄호에서 계산된 값(lst[i])값을 현재 값(cur_val)로 저장해주고
    # lst[i-1] 값과 cur_val를 더해서 lst[i-1]에 저장해준다.
    # lst[i]는 0으로 초기화 시킨다.(다음 새로운 괄호가 나오면 해당 인덱스번째가 사용되어야 하므로)
    elif chemical[idx] == ')':
        cur_val = lst[i]
        lst[i] = 0
        i -= 1
        lst[i] += cur_val
    # 조건문이 모두 끝나면 다음 식의 요소를 판단하기 위해 idx +1 증가
    idx += 1

# while문이 모두 끝나면 각 괄호의 값을 저장한 lst의 합을 구한다.
print(sum(lst))


```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" width="20" height="20">[[12789]도키도키 간식드리미](https://www.acmicpc.net/problem/12789)

```python
import sys
input = sys.stdin.readline

N = int(input())
# 현재 서있는 줄
line = list(map(int, input().split()))
# stack 구조로 만들어주기 위해 line을 reverse
line.reverse()
# 현재 서 있는 줄에서 옮겨갈 수 있는 대기 줄
waiting = []

# 번호표가 1번 부터 시작하므로
n = 1
# 번호표가 N이 될때까지 while문
while n < N+1:
    # line에 사람이 있고, line의 마지막 번호가 현재 번호(n)라면
    # 그 번호를 pop해서 빼주고 번호표 +1(다음 사람) 해준다.
    if line and line[-1] == n:
        line.pop()
        n += 1
    # line에 사람이 없거나 line의 마지막 번호가 현재 번호(n)가 아니라면 다음으로 waiting에서 찾음
    # waiting에 사람이 있고 현재 번호(n)을 가진 사람이 있다면 pop해주고
    # 번호표(n)을 +1 해줌
    elif waiting and waiting[-1] == n:
        waiting.pop()
        n += 1
    # 위 조건을 만족하진 않지만 (즉, 통로로 나올 수 있는 사람 중에 현재 번호를 가진 사람이 없다면)
    # line의 마지막에 있는 사람을 waiting으로 옮겨준다.
    elif line:
        waiting.append(line.pop())
    # 위 조건을 모두 만족하지 않는다면(즉, line에 사람이 없고 waiting 마지막 번호가 현재번호와 일치하지 않는다면)
    # 이는 순서대로 간식을 받을 수 없다는 뜻이므로 break로 while문을 빠져나옴
    elif waiting:
        break
# line과 waiting 줄이 다 비어야 간식 받을 수 있음
if not line and not waiting:
    print('Nice')
else:
    print('Sad')
```



###   <img src="https://d2gd6pc034wcta.cloudfront.net/tier/12.svg" width="20" height="20">[[17298]오큰수](https://www.acmicpc.net/problem/17298)

### 시간초과 코드입니다..

```python
# 시간초과
# 스택으로 어떻게 풀어야될지 모르겠어요,,
import sys
input = sys.stdin.readline


def nge(numbers, idx):
    base = numbers[idx]
    for i in range(idx+1, N):
        if base < numbers[i]:
            return numbers[i]
    return -1


N = int(input())
nums = list(map(int, input().split()))
for i in range(N):
    result = nge(nums, i)
    print(result, end=' ')
print()
```

