# 첫번째 줄에 빌딩의 개수 N
# 두번째 줄부터 N+1번째 줄까지(N개의 줄만큼) 각 빌딩의 높이 h가 주어진다.
# 각 빌딩은 오른쪽으로 검사할수 있으며 자기보다 빌딩이 몇개인지 찾아보자

# import sys
# N = int(sys.stdin.readline())
# data = [int(sys.stdin.readline()) for _ in range(N)]
# result = [0]*N
# for i in range(N):
#     for j in range(i+1,N):
#         if data[i] > data[j]:
#             result[i] += 1
#         else:
#             break
# print(sum(result))
# 이중 for문은 시간초과
# 실패, 다른방법으로 해보자
########################################################################

# 풀이
# 1. 스택이 비어있지않고 스택의 마지막값이 비교할 값보다 작으면 계속해서 pop 하는 while
# 2. while 조건에 안걸린다면 stack의 길이를 value에 누적합 하고 현재 빌딩을 스택에 push
# stack의 길이만큼을 누적합 하는 이유 : stack에 남아있는 애들은 현재 검사하는 빌딩(i)를 볼수 있기 때문, 빌딩 i가 하나씩 붙으면 stack에서 보는 애들이 +1 씩 누적합 되는 느낌 (stack에 있는 애들 갯수만큼 계속 더해줌)
# 즉, 얘(i)를 보고있는 빌딩의 갯수가 몇개인지 매번 확인!!

# 입력값 N 6 빌딩(10,3,7,4,12,2)가 주어졌을때
# stack
# 10 (stack의 길이먼저 더한 후에 push 이기 때문에 길이 0, 10을 push)
# 10 3 (10이 볼수있음,길이 1)
# 10 7 (3은 pop하고 나서 계산: 10이 7을 볼수있음,길이 1)
# 10 7 4 ( 10과 7이 4를 볼수 있음,길이 2)
# 12 (12보다 작은값 모두 pop 후에 다시 계산,아무도 12를 볼수없음 길이 0)
# 12 2 (12는 2를 볼수있음, 길이 1)
# 총합 길이 5


import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
value = 0

for i in range(N): # i 는 현재 검사할 빌딩
    while stack and stack[-1] <= data[i]:
        stack.pop()
    value += len(stack)
    stack.append(data[i])

print(value)
