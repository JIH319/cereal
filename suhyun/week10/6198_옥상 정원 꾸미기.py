# 6198. 옥상 정원 꾸미기
import sys
input = sys.stdin.readline

N = int(input()) # 빌딩의 개수 N
floor = [int(input()) for _ in range(N)]
result = 0
# for i in range(N-1):
#     for j in range(i+1,N):
#         if floor[i] > floor[j]:
#             result += 1
#         else:
#             break
# print(result)
stack = []
for i in range(N):
    # 스택이 존재하고, 이전 탑이 현재탑 보다  크거나 작을경우 쓸모가 없다. 버려주자.
    while stack and stack[-1] <= floor[i]:
        stack.pop()
    stack.append(floor[i])
    # stack 에 있는 친구들은 현재 탑보다 큰친구들밖에 안남아있다, 현재 큰탑 을 뺴야하므로 -1 해준 값을 더해준다.
    result += len(stack) - 1

# 총체적으로 구한 result 를 append 한다.
print(result)