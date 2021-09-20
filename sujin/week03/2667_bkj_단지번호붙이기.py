import sys

def bfs(r,c):
    # 같은 단지에는 같은 숫자(1과 혼동하지 않기 위해 2부터)를 붙여준다
    global num
    num += 1
    visited[r][c] = num
    # 단지 내 주택 수 세기
    cnt = 1
    q = []
    q.append((r,c))
    while q:
        cr, cc = q.pop()
        # 집은 상우하좌 네가지 방향으로만 인정
        for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr, nc = cr+di, cc+dj
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = num
                cnt += 1
    return cnt  

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
num = 1
result = []
for i in range(N):
    for j in range(N):
        # 주택이 있고, 다른 단지에 포함되지 않은 주택이면 
        if arr[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))

print(num-1)
result.sort()
for e in result:
    print(e)