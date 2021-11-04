# # N권의 교과서, 1~N까지 번호
# # 맨위에 있는 교과서만 꺼낼 수 있음
# # 꺼낸 순서대로 나열해야함 >> 번호 순으로 나열할 수 있는지 여부를 알려주는 프로그램 작성
# import sys
# from collections import deque

# # N: 교과서의 수, M:교과서 더미의 수
# N,M = map(int,sys.stdin.readline().split())
# # 더미별로 모아 만든 2차원 deque
# book = deque()
# # 맨위 번호만 모은 deque
# top = deque()
# for i in range(M):
#     _ = int(sys.stdin.readline())
#     tmp = deque(map(int, sys.stdin.readline().split()))
#     book.append(tmp)

# # result : 1이면 번호순 나열 가능, 0이면 불가능
# result = 1
# # num : 현재 찾아야 할 번호 (1~N)
# num = 1
# while num < N+1:
#     for i in range(M):
#         # 더미에 책이 존재하고, 맨위의 책 번호가 찾는 번호라면
#         # >> 다음 num 을 찾기 위해 for문 탈출
#         if book[i] and book[i][-1]:
#             book[i].pop()
#             num += 1
#             break
#     # for문에서 찾지 못하고 나왔다면, 번호순 나열 불가능
#     else:
#         break
# if result:
#     print('yes')
# else:
#     print('no')




# N권의 교과서, 1~N까지 번호
# 맨위에 있는 교과서만 꺼낼 수 있음
# 꺼낸 순서대로 나열해야함 >> 번호 순으로 나열할 수 있는지 여부를 알려주는 프로그램 작성
import sys
from collections import deque

# N: 교과서의 수, M:교과서 더미의 수
N,M = map(int,sys.stdin.readline().split())
# 더미별로 모아 만든 2차원 deque
book = deque()
# key : 맨 위의 수, val: (몇번째더미, 높이)
top_book ={}

for i in range(M):
    K = int(sys.stdin.readline())
    tmp = deque(map(int, sys.stdin.readline().split()))
    # key : 맨 위의 수, val: (몇번째더미, 높이)
    top_book[tmp[-1]]= (i,K-1)
    book.append(tmp)

result = 1
# i : 현재 찾아야 할 번호 (1~N)
for i in range(1,N):
    # 맨위에 찾아야할 번호 있음
    if i in top_book.keys():      
        # i : 찾는 수를 키로 하는 값 꺼내서, 
        idx, height = top_book[i]
        top_book.pop(i)
        # idx번째 더미에 책 남아있다면
        if height:
            # tmp : 맨 위 책 번호
            tmp = book[idx][height-1]
            top_book[tmp] = (idx,height-1)
    # 찾아야할 번호 없음
    else:
        result = 0
        break
        
if result:
    print('Yes')
else:
    print('No')
