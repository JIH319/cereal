from collections import deque
def bfs(r,c):
    queue = deque()     # deque 선언
    queue.append((r,c,0))   # L을 찾은 행,열,지나간 거리를 저장(시작 거리는 0)
    visited = [[0]*M for _ in range(N)] # 지나갔던 경로를 저장하기 위한 2차원 배열
    visited[r][c] = 1   # 현재 자리 방문했다는 표시로 1로 변경
    path = []   #   지나간 경로들을 저장하기 위한 path
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    while queue:    # 더이상 갈 경로가 없을때 까지
        cr,cc,dis = queue.popleft() # 현재 좌표와 현재 지나간 거리
        path.append((cr,cc,dis))    # popleft 할때마다 지나간 path에 해당 좌표와 거리 저장
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0<= nc < M and arr[nr][nc] =='L' and not visited[nr][nc]:    # 범위를 벗어나지 않고 이동하려는 곳이 L이며 방문하지 않았다면
                queue.append((nr,nc,dis+1)) # 거리 +1을 저장한 이동한 좌표를 큐에 저장
                visited[nr][nc] = 1 # 방문표시
    return path[-1] # 가장 마지막에 방문한 좌표와 거리를 반환

N,M = list(map(int,input().split()))
arr = [list(input()) for _ in range(N)]


max_val = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            val = bfs(i,j)
            if val[2] > max_val:    # 계속해서 반환해 내는 path의 2번째 값인 거리값을 최대값 찾기위한 조건문
                max_val = val[2]
print(max_val)

