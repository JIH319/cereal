# 17298. 오큰수
import sys
from collections import deque
N = int(sys.stdin.readline())  # 크기가 N인 수열

arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
stack = deque([0])
for i in range(1,N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
print(*result)
