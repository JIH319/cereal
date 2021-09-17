## #1218_괄호짝짓기

```python
for i in range(1,11):
    N = int(input())
    data = input()
    stack = []
    opendata = ['<','(','[','{']

    top = -1
    result = 1
    for j in range(N):
        # 여는 괄호일때
        if data[j] in opendata:
            top += 1
            stack.append(data[j]) 
            
        # 닫는 괄호일때
        else:
            if data[j] == '>':
                if stack[top] != '<':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()
            
            if data[j] == ')':
                if stack[top] != '(':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()

            if data[j] == ']':
                if stack[top] != '[':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()

            if data[j] == '}':
                if stack[top] != '{':
                    result = 0
                    break
                else:
                    top -= 1
                    stack.pop()
    print('#{} {}'.format(i,result))
```





## #10773_제로

```python
import sys

data = []
result = 0
N = int(sys.stdin.readline())
for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    # 새로 들어온 변수가 0이면, 리스트 마지막값 빼기
    if temp == 0 and data:
        result -= data.pop()
    # 0아니면 리스트에 담기
    else:
        result += temp
        data.append(temp)
print(result)
```

