# 1012. 유기농 배추
```python
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x):
    q = deque([(y, x)])
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0<=nr<n and 0<=nc<m and maps[nr][nc]:
                maps[nr][nc] = 0
                q.append((nr, nc))


for tc in range(int(input())):
    m, n, k = map(int, input().split())
    maps = [[0]*m for _ in range(n)]
    worm = 0
    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1

    for i in range(n):
        for j in range(m):
            if maps[i][j] :
                worm += 1
                dfs(i, j)
    print(worm)
```

# 2056. 연월일 달력
```python
for tc in range(1, int(input())+1):
    days = input()
    y = days[:4]
    m = days[4:6]
    d = days[6:]
    check = False
    if int(m) < 1 or int(m) > 12:
        check = True
    if m == '02' and int(d) > 28:
        check = True
    if int(d) < 1 :
        check = True
    if m in ('01', '03', '05', '07', '08', '10', '12') and int(d) > 31:
        check = True
    if m in ('04', '06', '09', '11') and int(d) > 30:
        check = True
    if check:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, '/'.join([y, m, d])))
 ```


# 16235. 나무 재테크
```python
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                new_tree = []
                for d in range(len(trees[i][j])):
                    if maps[i][j] >= trees[i][j][d]:
                        maps[i][j] -= trees[i][j][d]
                        new_tree.append(trees[i][j][d]+1)
                    else:
                        dead_trees[i][j].append(trees[i][j][d])
                trees[i][j] = new_tree


def summer():
    for i in range(n):
        for j in range(n):
            if dead_trees[i][j]:
                for d in range(len(dead_trees[i][j])):
                    maps[i][j] += dead_trees[i][j][d]//2


def autumn():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age%5 == 0 :
                        for d in range(8):
                            ni = i + dy[d]
                            nj = j + dx[d]
                            if 0 <= ni < n and 0 <= nj < n:
                                trees[ni][nj].append(1)


def winter():
    for i in range(n):
        for j in range(n):
            maps[i][j] += A[i][j]


def print_trees():
    for i in range(n):
        print(*trees[i])


# r, c는 1부터 시작함 -> -1 해주기
n, m, k = map(int, input().split())
# 밭
maps = [[5]*n for _ in range(n)]
# 추가 양분
A = [list(map(int, input().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(k):
    dead_trees = [[[] for _ in range(n)] for _ in range(n)]
    spring()
    summer()
    autumn()
    winter()

answer = 0
for i in range(n):
    for j in range(n):
        if trees[i][j]:
            answer += len(trees[i][j])

print(answer)
```
