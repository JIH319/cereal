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
