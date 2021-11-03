

# 자료구조는 최고 아니야

```python
"""
4 2
2
3 1
2
4 2

5 2
3
3 5 1
2
4 2
"""
# 생각해보니... 모든 숫자가 다 들어오는데 오름차순으로만 돼있으면 되네...
# 다음 숫자가 크면 무적권 탈락이네
import sys

n,m = map(int,sys.stdin.readline().split())
result = 'Yes' # 기본 결과값을 두고 아닌 케이스에만 'No'로 해야겠다.
for i in range(m):
    k = int(sys.stdin.readline())
    ki = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(k-1): # 자기와 자기다음꺼만 비교하므로 k-2인덱스 까지만 확인
        if ki[j] < ki[j+1]: # 다음꺼가 크면 타타탙타탈락
            result = 'No' # 노로 바꾸기

print(result)

```



# 천재 수학자 성필

```python
"""
123*+
"""
#이거는 수업시간에 과제로 해본거 같은 느낌적인 느낌쓰

stack = []

for i in input():
    if i.isdigit(): #숫자면 담고
        stack.append(int(i))
    else: #아니면 팝팝해서 순서 잘 생각해서 연산 
        num1 = stack.pop()
        num2 = stack.pop()
        if i == '+':
            stack.append(num2+num1)
        elif i == '-':
            stack.append(num2-num1)
        elif i == '*':
            stack.append(num2*num1)
        else:
            stack.append(num2/num1)

print(int(*stack))
```

# 균형잡힌 세상

```python
#런타임에러;;
"""
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
"""
while True:
    stack = []
    result = 'yes'
    for i in list(input()): #인풋된거 돌면서
        if i != '.' and i in ['[', '(',')', ']']: #.이아니고 괄호면 
            if not stack or i in ['[', '(']: # 비어있고 여는 괄호들이면
                stack.append(i) #어펜
            if i == ']' and stack[-1] == '[': # 닫는 대괄호이고 스택의 젤 위가 여는 대괄호이면
                stack.pop() #팝
            if i == ')' and stack[-1] == '(': # 닫는 소괄호이고 스택의 젤 위가 여는 소괄호이면
                stack.pop()

    if stack: #남아있으면 
        result = 'no' #노로 바꿔주고
    print(result)
```



# 화학식량

```python
#왜 안되는고니..
data = {'H': 1, 'C': 12, 'O': 16}
while True:
    stack = []
    tmp = 0
    for i in input():
        if i == '(': #여는 괄호면
            stack.append(i) #넣고
        if i in data.keys(): #키에 해당되는 값이면
            stack.append(data[i]) #그 밸류값을 스택에 넣고
        if i == ')': #닫는 괄호면
            while True: 
                if stack.pop() == '(': #팝한게 여는 괄호일때까지 와일
                    break 
                tmp += stack.pop() #그게아니면 tmp에 숫자들을 다 더해준다
            stack.append(tmp) # 여는 괄호를 만나서 나왔을때 tmp에 있는 값이 다시 스택에 어펜드
        if 2 <= int(i) <= 9: # 숫자가 나왔을때는
            stack.append(stack.pop() * int(i)) # 숫자 바로 앞의 값을 곱해줘서 다시 어펜드
            
    print(sum(stack)) # 스택에 남은 숫자들을 다 더한다
```



# 오키도키 간식드리미

```python
#런타임에러 풍년이롤세....

"""
5
5 4 1 3 2
"""
# 그 정렬한 값이 다 돌고난 뒤의 값과 동일하면 나이스로 하자
N = int(input())
line1 = list(map(int,input().split()))
line2 = sorted(line1,reverse=True)
# print(line2)
# print(line1)
stack = []
tmp = []
for i in line1:
    if not stack: #비었으면
        stack.append(i) # 스택에 넣고
    else: #안비었을때
        if stack[-1] > i: # 젤위의 값이 더 크면  
            stack.append(i) # 어펜드
        else: # 작은 값이 위에 있다면
            while stack[-1] < i: # 내가 더 클때까지
                num = stack.pop() # 그 수들을 팝해서 tmp에 넣어두고
                tmp.append(num)
            else: #크게 되었을때 나도 스택에 어펜드
                stack.append(i)
while tmp: # 티엠피 비워서 스택에 넣기
    a = tmp.pop()
    stack.append(a)
# print(stack)

if stack == line2: #같으면 나이스
    print("Nice")
else: #아니믄 새드드
    print("Sad")
```



# 오~큰수

```python
"""
4
3 5 2 7

4
9 5 4 8

5 7 7 -1

-1 8 8 -1
"""
#이건 또 왜 시간초과야...
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
# print(data)

for i in range(len(data)): #인덱스로 접근..
    stack = []
    for j in range(i+1, len(data)): # i다음부터 끝까지
        if data[i] < data[j]: #큰것만 스택에 모으고
            stack.append(data[j])
    if stack: #모은것중에 젤 앞에꺼
        print(stack[0],end=" ")
    else: #빈 스택이면 -1출력
        print(-1, end=" ")
```



# 스택

```python
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
"""
import sys

input = sys.stdin.readline
N = int(input())
stack = []

for i in range(N):
    data = input().split()
    # print(data)
    if data[0] == 'push':
        stack.append(data[1])
    if data[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    if data[0] == 'size':
        print(len(stack))
    if data[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if data[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

```





