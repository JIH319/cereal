def BFS(x,y):
    global worm
    dx = [-1,1,0,0] # 상 하 좌 우
    dy = [0,0,-1,1]
    # 한번 호출될때마다 벌레 투입
    worm += 1

    queue = []
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        cx,cy = queue.pop()

        for d in range(4):
            nx = cx+dx[d]
            ny = cy+dy[d]

            if 0<=nx < N and 0 <= ny < M and not visited[nx][ny] and farm[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = 1



T=int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split()) # N 세로길이 M 가로길이 K 배추의 위치 개수
    xy = [list(map(int,input().split())) for _ in range(K)] # xy 변수에 K개의 좌표 담기
    farm = [[0]*M for _ in range(N)]    # 우선 빈 밭을 생성
    visited = [[0]*M for _ in range(N)] # 방문체크 할 리스트 생성
    worm = 0   

    for x,y in xy:        # K개의 좌표를 밭에 표시
        farm[x][y] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and not visited[i][j]: # 방문한적 없고 배추가 있다면
                BFS(i,j)
    print(worm)
