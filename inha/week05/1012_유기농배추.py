import sys

input = sys.stdin.readline


# dfs 이용
def dfs(s, e):
    global cnt
    adj[s][e] = 0
    stack = [(s,e)]
    while stack:
        c = stack[-1]
        ci, cj = c[0], c[1]
        # 상하좌우로 옮겨갈 수 있는 배추가 있는지 확인
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < M and adj[ni][nj]:
                adj[ni][nj] = 0 # 이미 방문한 배추는 0이로 인접행렬에 표시해줌
                stack.append((ni, nj))
                break
        else: # 상하좌우로 더이상 연결된 배추가 없음
            stack.pop()
    cnt += 1


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    adj = [[0]*M for _ in range(N)] # N X M 의 인접행렬 만듦
    # input을 받아서 인접행렬에 배추가 있는 곳을 표시해줌
    for _ in range(K):
        j, i = map(int, input().split())
        adj[i][j] = 1
    cnt = 0
    i = 0
    while i < N:
        j = 0
        while j < M:
            # 인접행렬에서 1인 곳(배추가 있는 곳)을 찾음
            if adj[i][j] == 1:
                s, e = i, j
                dfs(i, j)
            j += 1
        i += 1
    print(cnt)

