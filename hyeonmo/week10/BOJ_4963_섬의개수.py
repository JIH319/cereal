# 첫째줄에 지도 너비 w와 높이 h가 주어지고 둘째줄 부터 h개 줄이 주어진다.
# 1은 땅 0은 바다
# 섬의 개수가 몇개인지 찾기, 섬이 이어져있으면 한개의 섬으로 친다.
def bfs(r,c):
    global ans
    visited[r][c] = 1
    ans += 1
    queue = [(r,c)]

    while queue:
        cr,cc = queue.pop(0)

        for d in range(8):
            nr = cr+dr[d]
            nc = cc+dc[d]

            if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and maps[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = 1



dr = [-1,1,0,0,-1,1,-1,1] # 상 하 좌 우 우상 우하 좌상 좌하
dc = [0,0,-1,1,1,1,-1,-1]

while True:
    W,H = map(int,input().split())
    if W != 0 and H != 0:
        maps = [list(map(int,input().split())) for _ in range(H)]
        visited=[[0]*W for _ in range(H)]
        ans = 0
        for i in range(H):
            for j in range(W):
                if maps[i][j] == 1 and not visited[i][j]:
                    bfs(i,j)
        print(ans)

    else:
        break