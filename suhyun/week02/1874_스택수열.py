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
