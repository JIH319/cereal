#### 1260. DFS 와 BFS

```python
# 1260. DFS 와 BFS
# [문제]
# 그래프를 DFS 로 탐색한 결곽와 BFS 로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 방문할 수 있는 정점이 여러개인 경우 -> 정점번호가 작은 것을 먼저 방문.
# 더 이상 방문할 수 없는 점은 종료.
# 정점 번호는 1번부터 N번 까지
import sys
from collections import deque
input = sys.stdin.readline


def dfs(s):
    # 방문했으니까 방문한곳은 1로 바꾸어준다.
    visited[s] = 1
    # 반복하면서, 방문할 수있지만 방문하지 않은 영역이면 조건문을 통과한다.
    for i in range(1,N+1):
        if adj[s][i] and not visited[i]:
            # 해당 영역 방문표시하고, 경로에 추가해주면서 재귀로 다음 영역을 간다.
            visited[i]=1
            dfs_rst.append(i)
            dfs(i)


def bfs(s):
    # 반복문으로돌리므로 que를 생성해준뒤, 이번엔 방문한 영역을 0으로 바꾸어준다.
    # 앞서 쓴 dfs visited를 재사용하기위해
    que = deque([s])
    visited[s]=0
    while que:
        r = que.popleft()
        # 반복문을 돌면서 방문할수 있으며 방문하지 않은 영역을 돌아준다.
        for i in range(1,N+1):
            if adj[r][i] and visited[i]:
                # dfs 에서 쓴 visited 를 그대로 쓰므로, 반대로 방문 영역을 0으로 둔다.
                visited[i]=0
                # 간 경로는 bfs_rst 에 추가해주면서, que 에 append 해준다.
                bfs_rst.append(i)
                que.append(i)


# [입력]
# 첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
# 인접 행렬로 갈 수 있는 영역울 표현해보자.
adj = [[0] * (N + 1) for _ in range(N + 1)]
# 적힌 노트들을 차례차례 입력해준다.
for _ in range(M):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1
# 방분영역, 방문했으면 1 안했으면 0
visited=[0]*(N+1)
# dfs 방문한 영역을 기록해줄 deque 생성
dfs_rst = deque([V])
# dfs 함수 실행
dfs(V)
# bfs 방문한 영역을 기록해줄 deque 생성
bfs_rst = deque([V])
# bfs 함수 실행
bfs(V)
# 주어진 결과들을 언패킹하여 출력하자.
print(*dfs_rst)
print(*bfs_rst)

```



#### 21736. 헌내기는 친구가 필요해

```python
# 21736_헌내기는 친구가 필요해
# 대학의 캠퍼스 N X M
# 상하좌우 이동
import sys
from collections import deque

input = sys.stdin.readline


# bfs 로 풀었는데...? 머지
def solve(r, c):
    # 사람만난 횟수를 체크하기 위한 cnt
    cnt = 0
    # 방문한 영역은 1로 표시~ que 는 deque 로 현재 위치를 que 에 삽입
    visited[r][c] = 1
    que = deque([(r, c)])
    # que 가 있는동안 반복문!
    while que:
        rr, cc = que.popleft()
        # 4방향 탐색!
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = rr + dr, cc + dc
            # 캠퍼스 영역을 안벗어나며 벽이아니고, 방문하지 않았으면 들어가는 조건문
            if 0 <= nr < N and 0 <= nc < M and campus[nr][nc] != 'X' and not visited[nr][nc]:
                # 그게 사람이면 cnt +=1 해주자
                if campus[nr][nc] == 'P':
                    cnt += 1
                # 방문했으니 1표시 que 에는 해당 영역 을 append 해주자
                visited[nr][nc] = 1
                que.append((nr, nc))
    return cnt


# [입력]
# 캠퍼스의 크기를 나타내는 두 정수 N 과 M
N, M = map(int, input().split())
# 캠퍼스의 정보 O: 빈 공간, X: 벽, I 는 도연이, P: 사람
campus = [list(input())[:M] for _ in range(N)]
# 시작지점을 받아주고, 찾은 경우 더 볼 필요 없으니 break 해주자
sr, sc = 0, 0
is_valid = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            sr, sc = i, j
            is_valid = 1
            break
    if is_valid:
        break
# 방문 영역을 담기 위한 2차원 배열
visited = [[0] * M for _ in range(N)]
# 반환값을 result 에 넣어주고, 해당 값이 있으면 출력 없으면 'TT' 출력하자
result = solve(sr, sc)
if result:
    print(result)
else:
    print('TT')

```



#### 1388. 바닥 장식

```python
# 1388. 바닥 장식
import sys

input = sys.stdin.readline


# 행 순회 해주고~
def row(rr, rc):
    # 행값 visited 쳐주고~
    visited[rr][rc] = 1
    # 행을 왔다갔다하자~
    for dc in [-1, 1]:
        nc = rc + dc
        # 범위를 안벗어나고 또 - 인데 방문 안했으면 다음 재귀~
        if 0 <= nc < M and floor[rr][nc] == '-' and not visited[rr][nc]:
            row(rr, nc)


# 열도 순회 해주고~
def col(cr, cc):
    # 열값 visited 쳐주고~
    visited[cr][cc] = 1
    # 열을 왔다갔다하자
    for dr in [-1, 1]:
        nr = cr + dr
        # 범위 안벗어나고 또 ㅣ 인데 방문 안했으면 다음 재귀~
        if 0 <= nr < N and floor[nr][cc] == '|' and not visited[nr][cc]:
            col(nr, cc)


# [ 입력 ]
N, M = map(int, input().split())
floor = [list(input())[:M] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        # 방문을 안했다~
        if not visited[i][j]:
            # 행을 봐야되나~
            if floor[i][j] == '-':
                result += 1
                row(i, j)
            # 열을 봐야되나~
            elif floor[i][j] == '|':
                result += 1
                col(i, j)
# 조건문이 돈 수만음 더한 값을 출력해주자~
print(result)

```



#### 4963. 섬의 개수

```python
# 4963. 섬의 개수
# 섬의 개수를 세는 프로그램을 작성하자.
import sys
from collections import deque

input = sys.stdin.readline


# 해결을 위한 solve 함수
def solve(r, c):
    # 방문표시 해주고~ que 에 값 너어주고~
    visited[r][c] = 1
    que = deque([(r, c)])
    # que 가 이는동안 반복문 돌아주고~
    while que:
        # 일딴 값을  빼주고
        rr, cc = que.popleft()
        # 값한번 돌아주고~ 8방향으로
        for dr, dc in [(1, 0),(1,-1), (-1, 0),(-1,-1), (0, 1),(1,1), (0, -1),(-1,1)]:
            nr, nc = rr + dr, cc + dc
            # 해당 값들이 방문할 수 있는데 방문을 안했을경우~
            if 0 <= nr < N and 0 <= nc < M and Island[nr][nc] and not visited[nr][nc]:
                # 방문하면서 que 에 더해주고~
                visited[nr][nc] = 1
                que.append((nr, nc))


# [입력]
# 00 을 만날때 까지는 계속 출력하자
while True:
    # N,M 을 받고ㅓ
    M, N = map(int, input().split())
    if not M and not M:  # 둘다 0이면 break!
        break
    # 반은 두개의 수로 지도를 그리자
    Island = [list(map(int, input().split()))[:M] for _ in range(N)]
    # 방문 영역을 표시해주고~
    visited = [[0] * M for _ in range(N)]
    # 출력할 값 result 생성~
    result = 0
    # 전체 섬 영역을 보면서, 섬이면서 방문을 안했으면~
    for i in range(N):
        for j in range(M):
            if Island[i][j] and not visited[i][j]:
                # 결과값 +1 해주고 solve 함수를 돌리자~
                result += 1
                solve(i, j)
    # 결과값 출력~!
    print(result)
```



#### 2606. 바이러스

```python
# 2606. 바이러스
import sys
from collections import deque

input = sys.stdin.readline


# 해결해줄 solve 함수~
def solve(sr):
    # 방문하면서 que 에 넣어주자~
    visited[sr] = 1
    que = deque([sr])
    # que 가 있는동안 반복 돌려주자~
    while que:
        r = que.popleft()
        # 반복문 으로 갈 수 있지만 안간 영역이 있으면 처리해주자~
        for nr in range(1, N + 1):
            if adj[r][nr] and not visited[nr]:
                # visited 에 1 해주고 que 에 append 해주자
                visited[nr] = 1
                que.append(nr)


# [입력]
N = int(input())  # 첫째 줄에는 컴퓨터의 수가 주어진다.
M = int(input())  # 쌍의 수 M
adj = [[0] * (N + 1) for _ in range(N + 1)]
# 쌍의 수 만큼 인접행렬을 만들어 주자.
for _ in range(M):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1
# 방문영역 표시해주자.
visited = [0] * (N + 1)
# solve 함수 불러주자 1에서 시작하는
solve(1)
# 출력은 visited 에서 방문한 영역(1) 의 값에서 1에서 시작한걸 뺴주자.
print(visited.count(1) - 1)


```



#### 2493. 탑

```python
# 2493. 탑
import sys
from collections import deque

input = sys.stdin.readline

# [ 입력 ]
N = int(input())  # 탑의 수
# 탑들의 영역 list
top = list(map(int, input().split()))
#  스택과 result 를 생성한다..
stack = []
result = [0] * N

# 0부터 N까지 반복문을 돌려준다.
for i in range(N):
    # 현재 탑의 크기를 불러온다.
    t = top[i]
    # 스택이 존재하고, 이전 탑이 현재탑 보다 작을경우 쓸모가 없다. 버려주자.
    while stack and top[stack[-1]] < t:
        stack.pop()
    # 스택 이 있는데 현재 탑보다 클 경우, 그 스택에 있는 탑의 위치를 result[i] 에 부여한다.
    if stack:
        result[i] = stack[-1] + 1
    # 다음 탑의 위치를 append 한다.
    stack.append(i)
# 총체적으로 구한 result 를 append 한다.
print(*result)


```



#### 6198. 옥상 정원 꾸미기

```python
# 6198. 옥상 정원 꾸미기
import sys
input = sys.stdin.readline

N = int(input()) # 빌딩의 개수 N
floor = [int(input()) for _ in range(N)]
result = 0
# for i in range(N-1):
#     for j in range(i+1,N):
#         if floor[i] > floor[j]:
#             result += 1
#         else:
#             break
# print(result)
stack = []
for i in range(N):
    # 스택이 존재하고, 이전 탑이 현재탑 보다  크거나 작을경우 쓸모가 없다. 버려주자.
    while stack and stack[-1] <= floor[i]:
        stack.pop()
    stack.append(floor[i])
    # stack 에 있는 친구들은 현재 탑보다 큰친구들밖에 안남아있다, 현재 큰탑 을 뺴야하므로 -1 해준 값을 더해준다.
    result += len(stack) - 1

# 총체적으로 구한 result 를 append 한다.
print(result)

```

