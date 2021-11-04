# 12789. 도키도키 간식드리미
from collections import deque
import sys
# [ 입력 ]
N = int(sys.stdin.readline()) # 현재 승환이의 앞에 서 있는 학생들의 수
arr = deque(list(map(int,sys.stdin.readline().split())))
stack = deque()
cnt = 1
while arr:
    if arr and cnt == arr[0]:
        arr.popleft()
        cnt += 1
    else:
        stack.append(arr.popleft())
    while stack and cnt == stack[-1]:
        stack.pop()
        cnt += 1
if stack:
    print('Sad')
else:
    print('Nice')
