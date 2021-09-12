# 사랑은 TIMING

```python
T = int(input())
for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    # if D >= 11 and H >= 11 and M >= 11: 왜 요곤 안될깡..
    result = (D-11)*1440 + (H-11)*60 + M-11
    a = result if result >= 0 else -1

    print('#{} {}'.format(tc, a))
```

# 보물섬

```python
import sys
input = sys.stdin.readline
from collections import deque


def bfs(r, c):
    queue = deque()
    queue.append((r, c, 0))
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    path = [] #경로를 넣을 곳

    while queue:

        cr, cc, distance = queue.popleft()  # index 0 가져와서 가능한 곳 찾기
        path.append((cr, cc, distance))

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            
            if 0 <= nr < N and 0 <= nc < M and treasure[nr][nc] == 'L' and not visited[nr][nc]:
                queue.append((nr, nc, distance + 1))
                visited[nr][nc] = 1

    return path[-1][2] #거리값만 가져오깅


N, M = map(int, input().split())
treasure = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'L': 
            length = bfs(i, j) #리턴값
            if length > result: #최댓값
                result = length

print(result)
```

