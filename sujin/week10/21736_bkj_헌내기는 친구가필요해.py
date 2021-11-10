# 캠퍼스 N*M
# O: 빈 공간, X: 벽, I: 도연, P: 사람 // I가 한 번만 주어짐
import sys
sys.setrecursionlimit(10**6)

dir = [(-1,0),(0,1),(1,0),(0,-1)] # 상우하좌 4방향

def dfs(r,c):
    # cnt : 만난 사람 수 
    cnt = 0
    stack = [(r,c)]
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1

    while stack:
        cr,cc = stack[-1]
        for dr,dc in dir:
            nr,nc = cr+dr,cc+dc
            # 범위안, 미방문, 벽아닌곳
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and campus[nr][nc] != 'X':
                # 사람이면
                if campus[nr][nc] == 'P':
                    cnt += 1
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        # 갈 수 있는 곳 없음 >> 직전 갈림길로 
        else:
            stack.pop()
    if cnt:
        print(cnt)
    else:
        print('TT')

def dfs_recursion(r,c):
    global count 
    seleted[r][c] = 1       # 방문표시
    if campus[r][c] == 'P': # 사람 만나면 count += 1
        count += 1
    # 상우하좌 4방향
    for dr,dc in dir:
        nr,nc = r+dr,c+dc
        # 범위안, 미방문, 벽아닌곳
        if 0<=nr<N and 0<=nc<M and not seleted[nr][nc] and campus[nr][nc] != 'X':
            dfs_recursion(nr,nc)

N,M = map(int,input().split())
campus = [input() for _ in range(N)]

count = 0
seleted = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            dfs(i,j)
            # dfs_recursion(i,j)
# if count:
#     print(count)
# else:
#     print('TT')
