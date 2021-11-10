## 1260_bkj_DFS와 BFS

```python
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과출력
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문 
# 더 이상 방문할 수 있는 점이 없는 경우 종료 
# 정점 번호는 1번부터 N번까지
# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V

def dfs(start):
    stack = [start]
    visited = [0]*(N+1)
    visited[start] = 1
    print(start,end=' ')
    while stack:
        cur = stack[-1]
        for i in range(1,N+1):
            # 현재 점에서 갈 수 있고, 미방문인 노드 찾으면 >> break
            # 갈 수 있으면 계속 ㄱㄱ
            if adj[cur][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                print(i,end=' ')
                break
        # 갈 수 있는 노드 없음 >> 직전 갈림길로 가서 다른 길 탐색
        else:
            stack.pop()

def dfs_recursion(current):
    selected[current] = 1
    print(current,end=' ')
    for i in range(1,N+1):
        if adj[current][i] and not selected[i]:
            dfs_recursion(i)


def bfs(start):
    q = [start]
    visited = [0]*(N+1)
    visited[start] = 1
    print(start,end=' ')

    while q:
        cur = q.pop(0)
        for i in range(1,N+1):
            # 방문 가능, 미방문 >> 현재 위치에서 갈 수 있으면 다 담기
            if adj[cur][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                print(i,end=' ')

N,M,V = map(int,input().split())
# 두 정점 사이 간선 여러개 있을 수 있음 & 양방향
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    adj[s][e] = 1
    adj[e][s] = 1

selected=[0]*(N+1)
dfs_recursion(V)
# dfs(V)
print()
bfs(V)

```





## 21738_bkj_헌내기는 친구가 필요해

```python
# 캠퍼스 N*M
# O: 빈 공간, X: 벽, I: 도연, P: 사람 // I가 한 번만 주어짐

dir = [(-1,0),(0,1),(1,0),(0,-1)] # 상우하좌 4방향

def dfs(r,c):
    # cnt : 만난 사람 수 
    cnt = 0
    stack = [(r,c)]
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1

    while stack:
        cr,cc = stack[-1]
        for dr,dc in dir:
            nr,nc = cr+dr,cc+dc
            # 범위안, 미방문, 벽아닌곳
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and campus[nr][nc] != 'X':
                # 사람이면
                if campus[nr][nc] == 'P':
                    cnt += 1
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        # 갈 수 있는 곳 없음 >> 직전 갈림길로 
        else:
            stack.pop()
    if cnt:
        print(cnt)
    else:
        print('TT')

# recursion error ;;...
import sys
sys.setrecursionlimit(10**6)
def dfs_recursion(r,c):
    global count 
    seleted[r][c] = 1       # 방문표시
    if campus[r][c] == 'P': # 사람 만나면 count += 1
        count += 1
    # 상우하좌 4방향
    for dr,dc in dir:
        nr,nc = r+dr,c+dc
        # 범위안, 미방문, 벽아닌곳
        if 0<=nr<N and 0<=nc<M and not seleted[nr][nc] and campus[nr][nc] != 'X':
            dfs_recursion(nr,nc)

            
N,M = map(int,input().split())
campus = [input() for _ in range(N)]

count = 0
seleted = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            dfs(i,j)
            # dfs_recursion(i,j)
# if count:
#     print(count)
# else:
#     print('TT')

```



## 1388_bkj_바닥장식

```python
def calc(target,r,c, arr):
    '''
    target: 현재 무시할 막대 (target에서 다른 막대 모양 될 때 count += 1)
    r: 세로 길이
    c: 가로 길이
    arr: 현재 바닥
    '''
    global count

    for i in range(r):
        remember = arr[i][0]
        # 가로막대로 시작했으면 일단 count 1
        if remember != target:
            count += 1
        for j in range(1,c):
            # 가로막대인데, 직전은 가로막대 X 
            # >> 방금 세로막대에서 가로막대로 바뀜 >> count += 1 
            if target != arr[i][j] and remember != arr[i][j]:
                count += 1
            remember = arr[i][j]

N,M = map(int,input().split())
# 세로:N 가로:M 
room = [input() for _ in range(N)]
# 세로:M 가로:N (원래 구조를 90도 돌림)
room2 = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        room2[i][j] = room[N-j-1][i]

count = 0
calc('|',N,M,room)
calc('-',M,N,room2)

print(count)
```





## 4963_bkj_섬의개수

```python

dir = [(-1,0),(0,1),(1,0),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)] # 상우하좌+대각선 8방향

def dfs(r,c):
    global cnt
    # dfs 호출 회수(cnt) == 섬의 개수
    cnt += 1

    stack = [(r,c)]
    while stack:
        cr,cc = stack[-1]
        for dr,dc in dir:
            nr,nc = cr+dr,cc+dc
            # 범위안, 미방문, 땅(1)
            if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and arr[nr][nc]:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        # 갈 수 있는 곳 없음 >> 직전 갈림길로 
        else:
            stack.pop()

while True:
    w,h = map(int,input().split())
    if not w and not h:
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            # 1:땅, 0:바다
            # 땅, 미방문이면 방문표시하러 dfs 호출
            if arr[i][j] and not visited[i][j]:
                dfs(i,j)
    print(cnt)
```





## 2606_bkj_바이러스

```python
#  한 컴퓨터가 웜 바이러스에 걸리면
#  그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스
# while 반복버전
def dfs():
    # 1번부터 출발하여 갈 수 있는 모든 점 세기
    cnt = 0
    stack = [1]
    visited = [0]*(N+1)
    visited[1] = 1

    while stack:
        cur = stack[-1]
        for i in range(1,N+1):
            # 방문 가능, 미방문
            if adj[cur][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                cnt += 1
                break
        else:
            stack.pop()
    print(cnt)

# 재귀 버전
def dfs_recursion(current):
    global count
    selected[current] = 1
    for i in range(1, N+1):
        # 방문가능, 미방문
        if adj[current][i] and not selected[i]:
            count += 1
            dfs_recursion(i)

# N: 컴퓨터의 수 (1번부터 N번까지), M : 연결 쌍의 수 
N = int(input())
M = int(input())

adj= [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    adj[s][e] = 1
    adj[e][s] = 1

dfs()

count = 0
selected = [0]*(N+1)
dfs_recursion(1)
print(count)
```





## 6198_bkj_옥상정원꾸미기

```python
# 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다
# 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 
# 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다

N = int(input())    # N : 빌딩의 개수
buildings = [0] * N # building : 빌딩 높이를 담는 배열
for i in range(N):
    buildings[i] = int(input())

buildings.append(1000000000) # 빌딩최대 높이 마지막에 추가
result = [0] * N    # index : 빌딩번호, value : 옥상 볼 수 있는 빌딩 개수
stack = [0]  # val : 빌딩번호(인덱스)
idx = 1
while stack and idx < N+1:
    
    # buildings[stack[-1]] : 현재 스택 마지막 빌딩의 높이
    # 같거나 더 높은 빌딩 나오면 >> 결과 배열 값 계산
    while stack and buildings[stack[-1]] <= buildings[idx]:
        result[stack[-1]] = idx - stack[-1] - 1
        stack.pop()
    
    # 더 작은 빌딩부터 계산
    stack.append(idx)
    idx += 1
    
# print(result)
print(sum(result))
```



## 2493_bkj_탑

```python
# 수평 직선의 왼쪽 방향으로 발사
# 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능

# N: 탑 개수, top : 탑들의 높이를 담는 배열
N = int(input())
top = list(map(int,input().split()))

result = [0] * N    # index: 레이저 출발점, val: 레이저 도착점(왼쪽에서 더 높은 탑의 번호) 
stack = [N-1]       # 현재 비교 기준이 될 (레이저 시작점) 담을 스택
idx = N-2
# 제일 오른쪽에서부터 왼쪽으로 진행
while stack and idx > -1:
    # 더 큰 탑을 발견하면, result에 기록
    while stack and top[stack[-1]] < top[idx]:
        result[stack[-1]] = idx+1   # 탑의 번호는 1~N
        stack.pop()
    
    stack.append(idx)
    idx -= 1
print(' '.join(map(str,result)))
```

