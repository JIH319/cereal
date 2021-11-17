# 6603 로또
import sys
from collections import deque

input = sys.stdin.readline


# 맞은거. dfs 로하자 s 는 시작지점, d는 길이
def dfs(s, d):
    # 길이가 6에 도달하면, 출력해주자
    if d == 6:
        print(*comb[:6])
        return
    # 반복문을 돌면서, 아직 확인안한 값들을 dfs 로 넘가주자
    for i in range(s, len(arr)):
        comb[d] = arr[i]
        dfs(i + 1, d + 1)


# 0 이 나올때까지 반복해야하므로, 반복문을 True 로 해주자.
while True:
    # 배열을 가져오되, 맨 왼쪽값을 날려버리자.
    arr = deque(list(map(int, input().split())))
    arr.popleft()
    # 그 깅ㄹ이에 맞게끔 조합 배열을 만들어주자.
    n = len(arr)
    comb = [0 for i in range(n)]
    # 길이가 0이면, 종료하자
    if not n:
        break
    # 시작지점 0, 길이 0부터 dfs 로 돌려주자.
    dfs(0, 0)
    print()
# 틀린거
#     result = []
#     for i in range(1 << n):
#         rst = []
#         for j in range(n):
#             if i & (1 << j):
#                 rst.append(arr[j])
#         # if len(rst)==6 and not rst in result:
#         if len(rst) == 6:
#             print(*rst)
#     print('')
