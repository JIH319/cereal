# 이것도 오큰수 비슷..!
import sys
input = sys.stdin.readline

N = int(input())
buildings = []
for _ in range(N):
    h = int(input())
    buildings.append(h)
# 빌딩 최고 높이가 1000000000
# 마지막에 최고 높이의 빌딩이 있다고 가정
buildings.append(1000000000)

# 인덱스 0 부터 시작
stack = [0]
# 합계 저장할 변수
result = 0

idx = 0
# 마지막 임의로 추가한 빌딩까지 N개이므로 range(1, N+1)
for i in range(1, N+1):
    # 자기 높이보다 낮은 빌딩 개수를 찾아야함
    # 자기보다 높거나 같은 빌딩이 오면 stack에서 pop하고 그 값을 idx에 저잘
    while stack and buildings[stack[-1]] <= buildings[i]:
        idx = stack.pop()
        # idx번째 빌딩은 idx+1부터 i-1번째까진 모두 자기보다 낮은 빌딩이었음
        # 따라서 합계를 저장하는 result에 (i-idx)-1을 더함
        result += (i - idx) - 1
    # 자기보다 낮은 빌딩이 오면 stack에 append
    stack.append(i)

print(result)