# 2606. 바이러스
import sys
from collections import deque

input = sys.stdin.readline


# 해결해줄 solve 함수~
def solve(sr):
    # 방문하면서 que 에 넣어주자~
    visited[sr] = 1
    que = deque([sr])
    # que 가 있는동안 반복 돌려주자~
    while que:
        r = que.popleft()
        # 반복문 으로 갈 수 있지만 안간 영역이 있으면 처리해주자~
        for nr in range(1, N + 1):
            if adj[r][nr] and not visited[nr]:
                # visited 에 1 해주고 que 에 append 해주자
                visited[nr] = 1
                que.append(nr)


# [입력]
N = int(input())  # 첫째 줄에는 컴퓨터의 수가 주어진다.
M = int(input())  # 쌍의 수 M
adj = [[0] * (N + 1) for _ in range(N + 1)]
# 쌍의 수 만큼 인접행렬을 만들어 주자.
for _ in range(M):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1
# 방문영역 표시해주자.
visited = [0] * (N + 1)
# solve 함수 불러주자 1에서 시작하는
solve(1)
# 출력은 visited 에서 방문한 영역(1) 의 값에서 1에서 시작한걸 뺴주자.
print(visited.count(1) - 1)
