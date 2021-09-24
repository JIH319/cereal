# 1은 집이 있는곳 0은 집이없는곳
# 연결된 집의 모임인 단지를 정의
# 단지가 몇개인지, 단지 내의 집이 몇개인지 확인하는 프로그램

def BFS(x,y):
    global visited
    global danji
    cnt = 0
    danji += 1
    queue = []
    queue.append((x,y))
    visited[x][y]=1
    dx = [-1,0,1,0] # 상 우 하 좌
    dy = [0,1,0,-1]

    while queue:
        cx,cy = queue.pop(0)
        cnt += 1
        
        for d in range(4):
            nx = cx+dx[d]
            ny = cy+dy[d]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = 1
    return cnt
    

N = int(input())
danji = 0
result = []
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            result.append(BFS(i,j))

print(danji)
result.sort()
print(*result,sep='\n')