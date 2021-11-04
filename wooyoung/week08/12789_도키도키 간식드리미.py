from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque(map(int, input().split())) #줄서있던 곳
stack = deque() #한사람만 서있을 수 있는 곳
i = 1 # 차례
while queue: #줄선 모든 사람들이 다 없어질 때까지
    if queue and queue[0] == i: #맨앞에 서 있는 사람이 호명될 사람이라면
        queue.popleft()         #꺼내주고
        i += 1                  #다음 호명자로 넘어간다
    else:                       #맨앞 사람이 호명될 사람이 아니라면
        stack.append(queue.popleft()) #stack에 넣기

    while stack and stack[-1] == i:   #stack 맨윗사람이 호명될 사람이라면
        stack.pop()                   #pop하고 다음 호명자로 넘어가기
        i += 1

if stack:
    print('Sad')
else:
    print('Nice')