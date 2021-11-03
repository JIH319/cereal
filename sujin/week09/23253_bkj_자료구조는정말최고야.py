# N권의 교과서, 1~N까지 번호
# 맨위에 있는 교과서만 꺼낼 수 있음
# 꺼낸 순서대로 나열해야함 >> 번호 순으로 나열할 수 있는지 여부를 알려주는 프로그램 작성
import sys
from collections import deque

# N: 교과서의 수, M:교과서 더미의 수
N,M = map(int,sys.stdin.readline().split())
# 더미별로 모아 만든 2차원 deque
book = deque()
# 맨위 번호만 모은 deque
top = deque()
for i in range(M):
    _ = int(sys.stdin.readline())
    tmp = deque(map(int, sys.stdin.readline().split()))
    book.append(tmp)

# result : 1이면 번호순 나열 가능, 0이면 불가능
result = 1
# num : 현재 찾아야 할 번호 (1~N)
num = 1
while num < N+1:
    for i in range(M):
        # 더미에 책이 존재하고, 맨위의 책 번호가 찾는 번호라면
        # >> 다음 num 을 찾기 위해 for문 탈출
        if book[i] and book[i][-1]:
            book[i].pop()
            num += 1
            break
    # for문에서 찾지 못하고 나왔다면, 번호순 나열 불가능
    else:
        break
if result:
    print('yes')
else:
    print('no')
