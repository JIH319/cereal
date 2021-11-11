# 2493. 탑
import sys
from collections import deque

input = sys.stdin.readline

# [ 입력 ]
N = int(input())  # 탑의 수
# 탑들의 영역 list
top = list(map(int, input().split()))
#  스택과 result 를 생성한다..
stack = []
result = [0] * N

# 0부터 N까지 반복문을 돌려준다.
for i in range(N):
    # 현재 탑의 크기를 불러온다.
    t = top[i]
    # 스택이 존재하고, 이전 탑이 현재탑 보다 작을경우 쓸모가 없다. 버려주자.
    while stack and top[stack[-1]] < t:
        stack.pop()
    # 스택 이 있는데 현재 탑보다 클 경우, 그 스택에 있는 탑의 위치를 result[i] 에 부여한다.
    if stack:
        result[i] = stack[-1] + 1
    # 다음 탑의 위치를 append 한다.
    stack.append(i)
# 총체적으로 구한 result 를 append 한다.
print(*result)
