from collections import deque
def bfs(r,c):
    # 현재위치에서 방문처리
    visited[r][c] = 1
    # 내 위치를 q에 담아야 한다!
    q = deque()
    q.append((r,c))
    # q가 없어질때까지 돌려!
    while q:
        # 현재 나의 위치에서
        cr, cc = q.popleft()
        # 상하좌우대각선 전부 둘러보기
        for k in range(8):
            nr = cr + dr[k]
            nc = cc + dc[k]
        # 범위 맞고, 방문 안햇고, 1 이면 고!
            if 0<= nr < h and 0 <= nc < w and not visited[nr][nc] and arr[nr][nc] == 1:
                q.append((nr,nc))
                visited[nr][nc] = 1

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    dr = [1,-1,0,0,-1,1,1,-1]
    dc = [0,0,1,-1,1,1,-1,-1]
    arr = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1

    print(cnt)