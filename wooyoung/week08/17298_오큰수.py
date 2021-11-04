
"""
# 시간초과 ㅜㅜ
import sys
from collections import deque

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
res = deque()
for i in range(N):
    for j in range(i, N):
        if nums[j] > nums[i]:
            res.append(nums[j])
            break
    else:
        res.append(-1)
print(*res)
"""

import sys

N = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for _ in range(N)]

stack.append(0)  # 오큰수를 찾아야할 숫자의 인덱스를 넣는 스택
i = 1
while stack and i < N:
    while stack and input[stack[-1]] < input[i]:
        # result >> 인덱스 : 오큰수 찾던 숫자, 값 : 오큰수
        result[stack[-1]] = input[i]
        stack.pop()

    stack.append(i)
    i += 1

for i in range(N):
    print(result[i], end=" ")