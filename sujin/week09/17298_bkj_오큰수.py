## 시간초과 ## 스택 어케 쓰지;;

import sys
from collections import deque

N = int(sys.stdin.readline())
data = deque(map(int,sys.stdin.readline().split()))


for i in range(N-1):
    for j in range(i+1,N):
        # 왼쪽에서부터 차례로 비교후
        # 첫 큰 수 결과값으로 담고 break
        if data[j] > data[i]:
            print(data[j],end=' ')
            break 
    else:
        print(-1,end=' ')
print(-1)


## 정답코드 (서치함)
import sys 
N = int(sys.stdin.readline()) 
input = list(map(int, sys.stdin.readline().split())) 
stack = [] 
result = [-1 for _ in range(N)] 
stack.append(0) # 오큰수를 찾아야할 숫자의 인덱스를 넣는 스택
i = 1 
while stack and i < N: 
    while stack and input[stack[-1]] < input[i]: 
        # result >> 인덱스 : 오큰수 찾던 숫자, 값 : 오큰수
        result[stack[-1]] = input[i] 
        stack.pop() 
     
    stack.append(i) 
    i += 1 

for i in range(N): 
    print(result[i], end = " ")
