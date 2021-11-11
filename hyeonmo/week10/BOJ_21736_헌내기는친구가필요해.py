# 캠퍼스는 N*M 크기
# 첫번째줄 N M 주어짐
# 두번째 줄부터 N개의 줄에 캠퍼스의 정보 주어짐
# O : 빈공간, X : 벽, I : 도연이, P : 사람
# 도연이가 만날수 있는 사람수 출력, 아무도 못만나면 TT 출력
# bfs

def bfs(r,c):
    ans = 0
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1

    queue = []
    queue.append((r,c))
    dr = [-1,1,0,0] # 상 하 좌 우
    dc = [0,0,-1,1]
    while queue:
        cr,cc = queue.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and campus[nr][nc] != 'X':
                # 조건 다 통과하고 넘어가려는 값이 p 일때만 카운트
                if campus[nr][nc] == 'P':
                    ans += 1
                queue.append((nr,nc))
                visited[nr][nc] = 1
    return ans

# 이중 반복문 break로는 안되니까 함수로 만들어서 return
def find_rc():
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                return bfs(i,j)


N,M = map(int,input().split())
campus = [list(input()) for _ in range(N)]
result = find_rc()
if result:
    print(result)
else:
    print('TT')

