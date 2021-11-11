# 1388. 바닥 장식
import sys

input = sys.stdin.readline


# 행 순회 해주고~
def row(rr, rc):
    # 행값 visited 쳐주고~
    visited[rr][rc] = 1
    # 행을 왔다갔다하자~
    for dc in [-1, 1]:
        nc = rc + dc
        # 범위를 안벗어나고 또 - 인데 방문 안했으면 다음 재귀~
        if 0 <= nc < M and floor[rr][nc] == '-' and not visited[rr][nc]:
            row(rr, nc)


# 열도 순회 해주고~
def col(cr, cc):
    # 열값 visited 쳐주고~
    visited[cr][cc] = 1
    # 열을 왔다갔다하자
    for dr in [-1, 1]:
        nr = cr + dr
        # 범위 안벗어나고 또 ㅣ 인데 방문 안했으면 다음 재귀~
        if 0 <= nr < N and floor[nr][cc] == '|' and not visited[nr][cc]:
            col(nr, cc)


# [ 입력 ]
N, M = map(int, input().split())
floor = [list(input())[:M] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        # 방문을 안했다~
        if not visited[i][j]:
            # 행을 봐야되나~
            if floor[i][j] == '-':
                result += 1
                row(i, j)
            # 열을 봐야되나~
            elif floor[i][j] == '|':
                result += 1
                col(i, j)
# 조건문이 돈 수만음 더한 값을 출력해주자~
print(result)
