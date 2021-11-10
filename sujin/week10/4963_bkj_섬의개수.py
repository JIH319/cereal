
dir = [(-1,0),(0,1),(1,0),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)] # 상우하좌+대각선 8방향

def dfs(r,c):
    global cnt
    # dfs 호출 회수(cnt) == 섬의 개수
    cnt += 1

    stack = [(r,c)]
    while stack:
        cr,cc = stack[-1]
        for dr,dc in dir:
            nr,nc = cr+dr,cc+dc
            # 범위안, 미방문, 땅(1)
            if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and arr[nr][nc]:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        # 갈 수 있는 곳 없음 >> 직전 갈림길로 
        else:
            stack.pop()

while True:
    w,h = map(int,input().split())
    if not w and not h:
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            # 1:땅, 0:바다
            # 땅, 미방문이면 방문표시하러 dfs 호출
            if arr[i][j] and not visited[i][j]:
                dfs(i,j)
    print(cnt)