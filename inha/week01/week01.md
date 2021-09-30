### [백준/2589] 보물섬

```python
from collections import deque


def bfs(s):  # m: map, s: 시작점 좌표
    visited = list([0] * width for _ in range(height))
    visited[s[0]][s[1]] = 1
    q = deque()
    q.append((s[0], s[1]))
    max_v = 0
    while q:
        c = q.popleft()
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # 시계방향
            ni = c[0] + di
            nj = c[1] + dj
            if 0 <= ni < height and 0 <= nj < width and not visited[ni][nj] and t_map[ni][nj] == 'L':
                q.append((ni, nj))
                visited[ni][nj] = visited[c[0]][c[1]] + 1
                if max_v < visited[ni][nj]:
                    max_v = visited[ni][nj]
    return max_v-1


height, width = map(int, input().split())
t_map = list((input()) for _ in range(height))
max_dis = 0

for i in range(height):
    for j in range(width):
        if t_map[i][j] == 'L':
            dis = bfs((i, j))
            if max_dis < dis:
                max_dis = dis
print(max_dis)
```



### [SWEA/4299] 태혁이의 사랑은 타이밍

```python
T = int(input())

for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    result = (D - 11) * 1440 + (H - 11) * 60 + (M - 11)
    if result < 0:
        timing = -1
    else:
        timing = result
    print('#{} {}'.format(tc, timing))
```

