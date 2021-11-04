def DFS(x,y,road,dump):
    global ans
    if road > ans:
        ans = road

    visited[x][y] = 1
    dx = [-1,0,1,0] # 상 우 하 좌
    dy = [0,1,0,-1] # 상 우 하 좌
  
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            # 현재 위치보다 가려는 곳이 작은값일때
            if arr[x][y] > arr[nx][ny]:
                DFS(nx,ny,road+1,dump)
            # 혹은 현재위치보다 높거나 같은 값일때는
            # 공사를 아직 안했고 현재값이 가려는곳을 공사한것보다 큰값이 된다면
            elif dump and arr[x][y] > arr[nx][ny] - K:
                tmp = arr[nx][ny]
                arr[nx][ny] = arr[x][y]-1
                DFS(nx,ny,road+1,0)
                arr[nx][ny] = tmp
    visited[x][y] = 0


T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_val = max(map(max,arr))

    visited = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val:
                DFS(i,j,1,1)
    print('#{} {}'.format(tc,ans))

