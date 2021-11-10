# 혹시 재귀 돌아가는 분 잇나요? 궁금하네요..
# 재귀로 해도 안돌아감, BFS, stack 풀이 가능
# 풀이법 1. BFS
from collections import deque
def bfs(r,c):
    global cnt
    q = deque()

    q.append((r,c))
    visited[r][c] = 1

    while q:
        # 현재 위치는 q의 가장 앞 아이
        cr, cc = q.popleft()
        # 현재 위치가 사람인 경우, cnt + 1
        if arr[cr][cc] == 'P':
            cnt += 1
        # 상하좌우로 살펴봐서 범위 벗어나지 않고, 방문하지 않고, X(못가는 곳)이 아니라면
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] != 'X':
                # q에 넣어주고 방문처리 해준다!
                q.append((nr,nc))
                visited[nr][nc] = 1


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dr = [1, 0, 0, -1]
dc = [0, 1, -1, 0]
# 만난 사람 수
cnt = 0
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 시작점 I
        if arr[i][j] == 'I':
            bfs(i,j)

if cnt:
    print(cnt)
else:
    print('TT')