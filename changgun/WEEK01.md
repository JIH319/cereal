### 보물섬

```python
from collections import deque
import sys

sys.stdin = open('input.txt')

def iter_bfs(start_i, start_j):
    queue = deque()
    queue.append((start_i, start_j))
    visited = [[-1] * m for _ in range(n)]
    visited[start_i][start_j] = 0
    while queue:
        oi, oj = queue.popleft()
        for k in range(4):
            ni = oi + di[k]
            nj = oj + dj[k]
            if ni not in range(0, n) or nj not in range(0, m):
                continue
            elif arrs[ni][nj] == 'L' and visited[ni][nj] == -1:
                visited[ni][nj] = visited[oi][oj] + 1
                queue.append((ni, nj))
    return visited[oi][oj]


n, m = map(int, input().split())
arrs = [list(input()) for _ in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

result = 0
for i in range(n):
    for j in range(m):
        if arrs[i][j] == 'L':
            result = max(result, iter_bfs(i, j))

print(result)
```



1. BFS로 L인 칸을 모두 순회 하고 가장 큰 값을 찾으려고 했는데 시간 초과 발생

2. 주어진 예제를 보면, (1, 0), (1, 1), (2,0) 처럼 순회하지 않아도 되는 노드가 있음. 왜냐하면 어떤 노드를 도착지로 삼던 (3,0) 에서 출발하는 것보다는 깊이가 깊을 수 밖에 없기 때문에

3. 덩어리로 쪼개는 게 가능 할 것 같은데, 어떻게 구현해야 할지 모르겠음

   

### 태혁이의 소개팅

```python
import sys

sys.stdin = open('input.txt')

blinddate = 11 * 60 * 24 + 11 * 60 + 11

for tc in range(int(input())):
    # d일 h시 m분
    d, h, m = map(int, input().split())
    dumped = d * 60 * 24 + h * 60 + m
    result = dumped - blinddate

    if result < 0:
        result = -1

    print('#{} {}'.format(tc+1, result)
```



​	1. 간단하게 분단위로 치환해서 빼주었음



​	

