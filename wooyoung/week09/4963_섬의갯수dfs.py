def dfs(r,c):
    # 현재위치에서 방문처리
    visited[r][c] = 1
    # 상하좌우대각선 전부 둘러보기
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        # 범위 맞고, 방문 안햇고, 1 이면 고!
        if 0<= nr < h and 0<= nc < w and not visited[nr][nc] and arr[nr][nc] == 1:
            dfs(nr,nc)

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
                dfs(i,j)
                cnt += 1

    print(cnt)