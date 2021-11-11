

# 헌내기

```python
# 도연이가 다니는 대학의 캠퍼스는 NXM 크기이며
# 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다.
# 불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력
# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐
# 단, 아무도 만나지 못한 경우 TT를 출력
"""
3 5
OOOPO
OIOOX
OOOXP

1

3 3
IOX
OXP
XPP

TT
"""

import sys
from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())

campus = [sys.stdin.readline().rstrip() for _ in range(N)]
sr, sc = 0, 0
for r in range(N):
    for c in range(M):
        if campus[r][c] == 'I':
            sr, sc = r, c

visited = [[0] * M for _ in range(N)]
visited[sr][sc] = 1
queue = deque([(sr, sc)])
result = 0
while queue:
    r, c = queue.popleft()
    for i in range(4):
        nr = r + direction[i][0]
        nc = c + direction[i][1]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if campus[nr][nc] == 'O':
                queue.append((nr, nc))
            elif campus[nr][nc] == 'P':
                queue.append((nr, nc))
                result += 1
            visited[nr][nc] = 1
print(result) if result else print('TT')
```



# DFS BFS

```python
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.

"""
4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4

5 5 3
5 4
5 2
1 2
3 4
3 1

3 1 2 5 4
3 1 4 2 5

1000 1 1000
999 1000

1000 999
1000 999
"""
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [0] * (N + 1)


def dfs(graph, V, visited):
    visited[V] = 1
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, V, visited):
    visited = [0] * (N + 1)
    queue = deque([V])
    visited[V] = 1

    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


dfs(graph, V, visited)
print()
bfs(graph, V, visited)
```

# 바닥장식

```python
# 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다.
# 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.
# 이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다.
# 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고,
# 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.
# 기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력
"""
4 4
----
----
----
----

4

6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-

31

7 8
--------
|------|
||----||
|||--|||
||----||
|------|
--------

13

10 10
||-||-|||-
||--||||||
-|-|||||||
-|-||-||-|
||--|-||||
||||||-||-
|-||||||||
||||||||||
||---|--||
-||-||||||

41

6 6
-||--|
||||||
|||-|-
-||||-
||||-|
||-||-

19
"""
# 행우선탐색과 열우선탐색으로 찾는데?

N, M = map(int, input().split())

data = [input() for _ in range(N)]
cnt = 0

for i in range(N):
    j = 0
    while j < M:
        if data[i][j] == '|':
            j += 1
        else:
            cnt += 1
            while j < M and data[i][j] == '-':
                j += 1


for j in range(M):
    i = 0
    while i < N:
        if data[i][j] == '-':
            i += 1
        else:
            cnt += 1
            while i < N and data[i][j] == '|':
                i += 1
print(cnt)

```



# 섬의 개수

```python
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
#  두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
#  지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
# 첫째 줄에는 지도의 너비 w와 높이 h
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.
"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

0
1
1
3
1
9
"""

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        (cr, cc) = queue.popleft()
        for i in range(8):
            nr = cr + dx[i]
            nc = cc + dy[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 1:
                    queue.append((nr, nc))
                    graph[nr][nc] = 0


while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    graph = []
    for i in range(N):
        data = list(map(int, input().split()))
        graph.append(data)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

```



# 바이러스

```python
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7

4
"""
N = int(input())
M = int(input())
graph = [[] * N for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (N + 1)


def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
```



# 탑

```python
# 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고,
# 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능
# 첫째 줄에 주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다.
# 만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력
"""
5
6 9 5 7 4

0 0 2 2 4
"""
N = int(input())
razer = list(map(int, input().split()))

stack = []
result = [0] * N
for i in range(N - 1, -1, -1):

    if not stack:
        stack.append((razer[i], i))
        continue

    while stack and stack[-1][0] < razer[i]:
        tower = stack.pop()
        result[tower[1]] = i + 1

    stack.append((razer[i], i))

print(*result)
```



# 옥상정원 꾸미기

```python
# 각 관리인들이 벤치마킹이 가능한 빌딩의 수의 합
# i번째 빌딩의 키가 hi이고, 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
# i번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+1, i+2, .... , N이다.
# 그런데 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다.
"""
6
10
3
7
4
12
2

5
"""
import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
stack = []
result = 0

for i in range(N):
    while stack != [] and stack[-1] <= data[i]:
        stack.pop()
    stack.append(data[i])
    result += len(stack)-1
print(result)
```





