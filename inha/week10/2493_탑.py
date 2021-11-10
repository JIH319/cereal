# 오큰수랑 푸는 방법 똑같,,
import sys
input = sys.stdin.readline
# 일직선 위에 N개의 높이가 서로 다른 탑 꼭대기에 송신기
# 왼쪽으로 송신
N = int(input())
heights = list(map(int, input().split()))

stack = [N-1]
ans = [0] * N

for i in range(N-2, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        ans[stack.pop()] = i+1
    stack.append(i)

print(*ans)