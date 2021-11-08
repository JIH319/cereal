# 1260. DFS와 BFS

```python
from collections import deque

n, m, v = map(int, input().split())
maps = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    maps[a][b] = 1
    maps[b][a] = 1


def dfs(v, visited):
    visited.append(v)
    for i in range(n+1):
        if maps[v][i] == 1 and (i not in visited):
            dfs(i, visited)
    return visited


def bfs(v) :
    q = deque()
    visited = [v]
    q.append(v)

    while q :
        c = q.popleft()
        for i in range(n+1):
            if maps[c][i] == 1 and (i not in visited):
                visited.append(i)
                q.append(i)
    return visited

print(*dfs(v, []))
print(*bfs(v))
```





# 21736. 헌내기는 친구가 필요해

```python
import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

# 전형적인 BFS 문제~ 상하좌우 확인하고 갈 수 있으면 q에 추가 아니면 pass~
# P 만나면 ans ++ 해준다
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

# for 문 2중으로 돌면서 도연이 위치 찾기 싫어서.. try-except 문을 썼다
for i in range(N):
    try:
        bfs(i, campus[i].index('I'))
        break
    except ValueError:
        continue

print(ans if ans else 'TT')
```



# 1388. 바닥 장식

```python
N, M = map(int, input().split())
room = [list(input()) for _ in range(N)]

# 이건 큐 문제가 아닌 거 같은디..

ans = 0
# for문안의 for문 말고도 두 개의 for문으로 나눠서 푸는게 시간이 덜 걸릴 듯
for i in range(N):
    for j in range(M):
        if room[i][j] == '-':
            for k in range(j, M):
                if room[i][k] != '-':
                    break
                room[i][k] = 'X'
            ans += 1
        elif room[i][j] == '|':
            for k in range(i, N):
                if room[k][j] != '|':
                    break
                room[k][j] = 'X'
            ans += 1

print(ans)
```



# 4963. 섬의 개수

```python
from collections import deque

# 8방향 다 봐야 함
dy = [0, 0, 1, -1, 1, -1, 1, -1]
dx = [1, -1, 0, 0, 1, -1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            # 땅이면 bfs 돌아주고 0으로 만들어줌 (방문 체크)
            if maps[i][j] == 1:
                q.append([i, j])
                maps[i][j] = 0
                while q:
                    y, x = q.popleft()
                    for k in range(8):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] :
                            q.append([ny, nx])
                            maps[ny][nx] = 0
                ans += 1
    print(ans)
```



# 2606. 바이러스

```python
# 유니온 파인드로도 풀리는 문제

def find_p(p, a):
    if p[a] != a :
        p[a] = find_p(p, p[a])
    return p[a]


def union_p(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)

    if a < b :
        parent[b] = a

    else:
        parent[a] = b


v = int(input())
e = int(input())

parent = [i for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    union_p(parent, a, b)

root = find_p(parent, 1)
cnt = 0
for i in range(2, v+1):
    if find_p(parent, i) == root :
        cnt += 1

print(cnt)
```

# 2493. 탑
```python
# 오큰수랑 똑같다 
N = int(input())
signal = [0]*N
top = list(map(int, input().split()))
stack = []
for i in range(N-1, -1, -1):
    while stack and top[i] > top[stack[-1]]:
        signal[stack.pop()] = i + 1
    stack.append(i)

print(*signal)
```



# 6198. 옥상 정원 꾸미기

```python
import sys
input = sys.stdin.readline
N = int(input())
buildings = [int(input()) for _ in range(N)]
stack = []
ans = 0
# 이것도 오큰수랑 비슷하네..

for i in range(N):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()

    stack.append(buildings[i])
    ans += len(stack) - 1

print(ans)
```

