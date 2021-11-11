# 1260. DFS 와 BFS
# [문제]
# 그래프를 DFS 로 탐색한 결곽와 BFS 로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 방문할 수 있는 정점이 여러개인 경우 -> 정점번호가 작은 것을 먼저 방문.
# 더 이상 방문할 수 없는 점은 종료.
# 정점 번호는 1번부터 N번 까지
import sys
from collections import deque
input = sys.stdin.readline


def dfs(s):
    # 방문했으니까 방문한곳은 1로 바꾸어준다.
    visited[s] = 1
    # 반복하면서, 방문할 수있지만 방문하지 않은 영역이면 조건문을 통과한다.
    for i in range(1,N+1):
        if adj[s][i] and not visited[i]:
            # 해당 영역 방문표시하고, 경로에 추가해주면서 재귀로 다음 영역을 간다.
            visited[i]=1
            dfs_rst.append(i)
            dfs(i)


def bfs(s):
    # 반복문으로돌리므로 que를 생성해준뒤, 이번엔 방문한 영역을 0으로 바꾸어준다.
    # 앞서 쓴 dfs visited를 재사용하기위해
    que = deque([s])
    visited[s]=0
    while que:
        r = que.popleft()
        # 반복문을 돌면서 방문할수 있으며 방문하지 않은 영역을 돌아준다.
        for i in range(1,N+1):
            if adj[r][i] and visited[i]:
                # dfs 에서 쓴 visited 를 그대로 쓰므로, 반대로 방문 영역을 0으로 둔다.
                visited[i]=0
                # 간 경로는 bfs_rst 에 추가해주면서, que 에 append 해준다.
                bfs_rst.append(i)
                que.append(i)


# [입력]
# 첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
# 인접 행렬로 갈 수 있는 영역울 표현해보자.
adj = [[0] * (N + 1) for _ in range(N + 1)]
# 적힌 노트들을 차례차례 입력해준다.
for _ in range(M):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1
# 방분영역, 방문했으면 1 안했으면 0
visited=[0]*(N+1)
# dfs 방문한 영역을 기록해줄 deque 생성
dfs_rst = deque([V])
# dfs 함수 실행
dfs(V)
# bfs 방문한 영역을 기록해줄 deque 생성
bfs_rst = deque([V])
# bfs 함수 실행
bfs(V)
# 주어진 결과들을 언패킹하여 출력하자.
print(*dfs_rst)
print(*bfs_rst)