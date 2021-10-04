import sys

direction = [(-1,0),(0,1),(1,0),(0,-1)]  # 상 우 하 좌

def worm(r,c):
    # 함수호출마다 cnt += 1
    global cnt
    cnt += 1

    q = [(r,c)]
    visited[r][c] = 1
    while q:
        cr,cc = q.pop(0)
        for dr, dc in direction:
            nr,nc = cr + dr, cc + dc
            # 배추위치 상우하좌에 있는 배추에 모두 방문 표시 
            # >> 한 지렁이가 갈 수 있다면 다시 함수호출 X
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = 1

T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    # M : 가로, N : 세로, K : 배추 개수
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)] # 방문 처리용 리스트

    # 배추 위치 입력받아 1로 저장    
    for _ in range(K):
        c,r = map(int,sys.stdin.readline().split())
        arr[r][c] = 1
    
    # 배열을 돌며 지렁이 필요 개수 알아내기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                worm(i,j)
    print(cnt)
