# swea 4299. 태혁이의 사랑은 타이밍

```python
def love(D, H, M):
    day = (D - 11) * 1440
    hour = (H - 11) * 60
    minute = M - 11

    result = day + hour + minute
    if result >=0:
        return result
    else:
        return -1

T = int(input())
for tc in range(1, T + 1):
    D, H, M = map(int, input().split())
    a = love(D,H,M)
    print('#{} {}'.format(tc, a))
```

느낀점 : 

불쌍한 태혁이,,처음에는 day, hour, minute 하나하나씩 다 if문을 걸었다가 문제가 요구하는건 전체 분이었기 때문에 전체 분을 먼저 구하고 조건문을 걸었다.



# 백준 2589. 보물섬

```python
# 백준 import sys + deque + pypy로 돌려야 실행시간초과가 안뜬다!
import sys
input = sys.stdin.readline
from collections import deque

def bfs(area, sr, sc):
    # deque 
    dq = deque([])
    dq.append((sr, sc))
    # 방문처리
    visited = [[0] * C for _ in range(R)]
    visited[sr][sc] += 1
    max = 0

    # 탐색방향 반시계방향
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    # bfs 시작
    while dq:  # dq가 비어있지 않으면 계속 수행
        # 큐의 front 가져와서 방문가능한 위치 찾기
        cr, cc = dq.popleft()
        # 현재위치에서 4방 탐색
        for q in range(4):
            nr, nc = cr + dr[q], cc + dc[q]
            # 갈 수 있는 경로인지 확인(정상범위, 미방문, 통로)
            if 0 <= nr < R and 0 <= nc < C and area[nr][nc] == 'L' and visited[nr][nc] == 0:
                # dq에 넣고 방문처리(거리를 구해야하기 때문에 +1)
                dq.append((nr,nc))
                visited[nr][nc] = visited[cr][cc] + 1
                # 최단거리 중 최대값 
                if visited[nr][nc] > max:
                    max = visited[nr][nc]

    return max

R, C = map(int,input().split())
max = 0
area = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if area[i][j] == 'L':
            sr, sc = i, j
            a = bfs(area, sr, sc)
            if a > max:
                max = a
#출발점에서 도착점까지 거리이기 때문에 -1 해줘야 한다.
print(max-1)
```

느낀점

bfs랑 최댓값 구하는걸 같이 해보니까 많이 배운것같다 뿌듯..^-^V