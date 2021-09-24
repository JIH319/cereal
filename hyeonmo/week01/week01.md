# 2589. 보물섬

```python
from collections import deque
def bfs(r,c):
    queue = deque()     # deque 선언
    queue.append((r,c,0))   # L을 찾은 행,열,지나간 거리를 저장(시작 거리는 0)
    visited = [[0]*M for _ in range(N)] # 지나갔던 경로를 저장하기 위한 2차원 배열
    visited[r][c] = 1   # 현재 자리 방문했다는 표시로 1로 변경
    path = []   #   지나간 경로들을 저장하기 위한 path
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    while queue:    # 더이상 갈 경로가 없을때 까지
        cr,cc,dis = queue.popleft() # 현재 좌표와 현재 지나간 거리
        path.append((cr,cc,dis))    # popleft 할때마다 지나간 path에 해당 좌표와 거리 저장
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0<= nc < M and arr[nr][nc] =='L' and not visited[nr][nc]:    # 범위를 벗어나지 않고 이동하려는 곳이 L이며 방문하지 않았다면
                queue.append((nr,nc,dis+1)) # 거리 +1을 저장한 이동한 좌표를 큐에 저장
                visited[nr][nc] = 1 # 방문표시
    return path[-1] # 가장 마지막에 방문한 좌표와 거리를 반환

N,M = list(map(int,input().split()))
arr = [list(input()) for _ in range(N)]


max_val = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            val = bfs(i,j)
            if val[2] > max_val:    # 계속해서 반환해 내는 path의 2번째 값인 거리값을 최대값 찾기위한 조건문
                max_val = val[2]
print(max_val)
```



# 4299. 태역이의 사랑은 타이밍

```python
T = int(input())
for tc in range(1,T+1):
    D,H,M = list(map(int,input().split()))

    meet_time = (11*24+11)*60+11    # 만나기로 한 11일 11시 11분이 총 몇분인지 계산
    taehyuk_time = (D*24+H)*60+M    # 깨달음을 얻은 날짜가 총 몇분인지 계산

    if taehyuk_time > meet_time:    # 깨달음을 얻은 시간이 더 나중이라면 만나기로한 시간 차감
        taehyuk_time -= meet_time
        print(f'#{tc} {taehyuk_time}')
    elif taehyuk_time == meet_time: # 같으면 0 낮으면 -1
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {-1}')

```

