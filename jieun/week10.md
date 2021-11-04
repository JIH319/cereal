# 21736. 헌내기는 친구가 필요해
```python
import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(si, sj):
    global ans
    q = deque([[si, sj]])
    visited = [[0]*M for _ in range(N)]
    visited[si][sj] = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            ny = dy[k] + r
            nx = dx[k] + c
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and campus[ny][nx] != 'X':
                if campus[ny][nx] == 'P':
                    ans += 1
                visited[ny][nx] = 1
                q.append([ny, nx])


N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    try:
        bfs(i, campus[i].index('I'))
        break
    except ValueError:
        continue

print(ans if ans else 'TT')
```
