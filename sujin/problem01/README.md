## 4299. 태혁이의 사랑은 타이밍

```python
def prayforhim(D, H, M):
    timing = (D-1) * 24 * 60 + H * 60 + M   # 깨달은 순간까지의 분
    promise = 10 * 24 * 60 + 11 * 60 + 11   # 약속시간까지의 분
    result = timing - promise
    if result < 0:
        return -1
    else:
        return result

for tc in range(1,int(input())+1):
    D, H, M = map(int, input().split())
    print('#{} {}'.format(tc,prayforhim(D, H, M)))
```







## 2589. 보물섬

```python
from collections import deque
# 상 우 하 좌
di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(i,j):
    maxv = 0
    visited = [[0]*c for _ in range(r)]
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr+di[i], cc+dj[i]
            if 0<= nr <r and 0<= nc <c and arr[nr][nc] == 'L' and not visited[nr][nc]:
                 visited[nr][nc] = visited[cr][cc] + 1
                 q.append((nr, nc))
                 # 가장 긴 시간 체크
                 if visited[nr][nc] > maxv:
                     maxv = visited[nr][nc]
    return maxv-1

r, c = map(int,input().split())
arr = [list(input()) for _ in range(r)]
result = 0
for i in range(r):
    for j in range(c):
        # 가장 긴 시간 갱신
        # 땅일때만 bfs 기록
        if arr[i][j] == 'L':
            temp = bfs(i,j)
            if temp > result:
                result = temp

print(result)
```

