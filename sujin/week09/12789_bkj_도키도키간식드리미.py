import sys
from collections import deque

N = int(sys.stdin.readline())
data = deque(map(int,sys.stdin.readline().split()))

stack = deque() # 대기열 LIFO
num = 1 # 현재 찾는 번호 (1부터 N까지 순서대로)
idx = 0 # 줄 인덱스
is_break = 0
result = 'Nice'
while True:
    # 줄 선 사람 다 대기줄로 뺐고
    if idx == N:
        # 대기줄 마지막들어간 사람이 찾는 번호 아니면 >>  불가능
        while stack:
            if stack[-1] == num:
                stack.pop()
                num += 1
            else:
                result = 'Sad'
                break
        # 줄선사람, 대기줄 모두 없음 >> while문 탈출
        break 
        
    # 아직 줄 선 사람 남아있음
    else:
        # 줄 선 곳에 찾는 번호 있음
        if data[idx] == num:
            idx += 1
            num += 1
        else:
            # 대기줄에 찾는 번호 있음
            if stack and stack[-1] == num:
                stack.pop()
                num += 1
            # 대기줄에도 찾는 번호 없음 >> 줄 선 사람 대기줄로 옮기기
            else:
                stack.append(data[idx])
                idx += 1

print(result)