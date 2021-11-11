# 1260. DFS와 BFS

```python
# DFS와 BFS로 탐색한 결과를 각각 출력
# 방문가능한곳이 한번에 여러곳이라면 가장 작은번호 먼저 방문
# 방문할수 있는곳이 없은경우 종료
# 정점 번호는 1번부터 N번 까지

# 첫째줄에 정점개수 N 간선개수 M 시작할 정점번호 V
# 이후 M개의 줄에 연결되어있는 두개의 정점번호 주어짐

from collections import deque

def dfs(v):
    result_dfs.append(v)
    visited[v] = 1
    for i in range(1,N+1):
        if arr[v][i] and not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        front = queue.popleft()
        result_bfs.append(front)
        for i in range(1,N+1):
            if arr[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1




N,M,V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    r,c = map(int,input().split())
    arr[r][c] = 1
    arr[c][r] = 1
visited = [0]*(N+1)
result_dfs = []
result_bfs = []
dfs(V)
print(*result_dfs)

visited = [0]*(N+1)
bfs(V)
print(*result_bfs)
```





# 21736. 헌내기는 친구가 필요해

```python
# 캠퍼스는 N*M 크기
# 첫번째줄 N M 주어짐
# 두번째 줄부터 N개의 줄에 캠퍼스의 정보 주어짐
# O : 빈공간, X : 벽, I : 도연이, P : 사람
# 도연이가 만날수 있는 사람수 출력, 아무도 못만나면 TT 출력
# bfs

def bfs(r,c):
    ans = 0
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1

    queue = []
    queue.append((r,c))
    dr = [-1,1,0,0] # 상 하 좌 우
    dc = [0,0,-1,1]
    while queue:
        cr,cc = queue.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and campus[nr][nc] != 'X':
                # 조건 다 통과하고 넘어가려는 값이 p 일때만 카운트
                if campus[nr][nc] == 'P':
                    ans += 1
                queue.append((nr,nc))
                visited[nr][nc] = 1
    return ans

# 이중 반복문 break로는 안되니까 함수로 만들어서 return
def find_rc():
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                return bfs(i,j)


N,M = map(int,input().split())
campus = [list(input()) for _ in range(N)]
result = find_rc()
if result:
    print(result)
else:
    print('TT')


```



# 1388. 바닥 장식

```python
# - 와 | 로 이루어진 배열이 주어짐
# - 는 행 방향으로 인접해 있으면 인접해 있는 모든 -를 한개로 친다.
# | 는 열 방향으로 위와 같다.
# N 행 개수 M 열 개수 N*M 의 배열

# dfs와 bfs로 구현하려면.. 넘어가기전 현재 문자열을 저장하고 넘겨준다..
# 또 다음 문자열로 넘어갈땐 넘어가기전 문자열 갱신..
# 네가지 방향으로 퍼져 나가기 때문에.. 그럼 길이는 어떻게 저장하지??
# 반복문으로 각 행을 검사하는게 더 쉬워보이는데 일단 해보자(정답처리 되었음)

# 풀이
# 이중 반복문으로 각 행을 검사하면서 - 이면 그 전과 비교
# | 이면 바로 위와 비교하여 같은값이라면 카운트 안하고 넘김 같은값이 아니라면 카운트
# 전 값을 비교할때 범위를 벗어나지 않게 조건처리

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
ans1 = 0
ans2 = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == '-':
            if 0 <= j-1 and arr[i][j-1] == '-':
                continue
            else:
                ans1 += 1
        else:
            if 0<= i-1 and arr[i-1][j] == '|':
                continue
            else:
                ans2 += 1
print(ans1+ans2)


```



# 4963. 섬의 개수

```python
# 첫째줄에 지도 너비 w와 높이 h가 주어지고 둘째줄 부터 h개 줄이 주어진다.
# 1은 땅 0은 바다
# 섬의 개수가 몇개인지 찾기, 섬이 이어져있으면 한개의 섬으로 친다.
def bfs(r,c):
    global ans
    visited[r][c] = 1
    ans += 1
    queue = [(r,c)]

    while queue:
        cr,cc = queue.pop(0)

        for d in range(8):
            nr = cr+dr[d]
            nc = cc+dc[d]

            if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and maps[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = 1



dr = [-1,1,0,0,-1,1,-1,1] # 상 하 좌 우 우상 우하 좌상 좌하
dc = [0,0,-1,1,1,1,-1,-1]

while True:
    W,H = map(int,input().split())
    if W != 0 and H != 0:
        maps = [list(map(int,input().split())) for _ in range(H)]
        visited=[[0]*W for _ in range(H)]
        ans = 0
        for i in range(H):
            for j in range(W):
                if maps[i][j] == 1 and not visited[i][j]:
                    bfs(i,j)
        print(ans)

    else:
        break
```



# 2606. 바이러스

```python
# 첫째줄 컴퓨터의 수 N
# 컴퓨터는 1번부터 번호가 매겨진다.
# 둘째줄에는 연결되어있는 컴퓨터의 쌍 수가 주어진다.
# 세번째 줄부터는 컴퓨터의 쌍 수 만큼 연결되어있는 컴퓨터 번호 쌍이 주어진다.

# 1번 컴퓨터가 바이러스 걸렸을때 1번컴퓨터와 연결되어있는 컴퓨터의 수를 출력하라
# bfs로도 풀수 있지만 dfs로 queue에 값이 들어갈때마다 카운트 해보자


def dfs(v):
    global ans
    visited[v] = 1
    for i in range(1,N+1):
        # v는 현재 컴퓨터 번호, v와 연결된 컴퓨터가 있는지 i로 검사한다.
        if computers[v][i] and not visited[i]:
            ans += 1
            dfs(i)



N = int(input())
M = int(input())
# 배열의 각 행의 순서를 컴퓨터 번호로 인식하기 위해 가로세로 N+1 만큼의 배열을 생성해준다.
computers = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):  # M개의 쌍을 만들어 놓은 computers 배열에 넣는다.(1 체크)
    com1,com2 = map(int,input().split())
    computers[com1][com2] = 1
    computers[com2][com1] = 1
visited = [0]*(N+1) # 방문체크할 배열
ans = 0
dfs(1)
print(ans)

```

# 2493. 탑
```python
# 첫째 줄에 탑의 수 N
# 두번째 줄에 탑의 높이가 적힌 값 한줄로 주어짐
# 탑은 오른쪽부터 왼쪽으로 현재 탑보다 더 높은 탑이 어디인지 위치값을 찾아내야한다.
# 위치 값은 1부터 시작한 값을 해당 위치에 넣는다.
# 오큰수,옥상정원 꾸미기와 비슷하게 풀어보자

# 풀이
# for 반복문을 오른쪽에서 왼쪽으로 가는데 결과값은 위치를 출력 해야 하니까
# i를 인덱스 값으로 활용
# stack이 비어있거나 stack의 마지막값 인덱스를 가진 탑과 현재 탑을 비교했을때 현재 탑이 더 작다면
# stack에 해당 인덱스(i)를 push
# stack에 값이 있고 현재 top이 stack의 마지막 값 인덱스를 가진 top보다 크다면
# result에 stack 마지막 인덱스와 동일한 위치에 현재위치 i + 1 을 넣어준다.
N = int(input())
top = list(map(int,input().split()))
result = [0]*N
stack = []
for i in range(N-1,-1,-1):
    while stack and top[i] > top[stack[-1]]:
        result[stack.pop()] = i + 1
    stack.append(i)

print(result)
```



# 6198. 옥상 정원 꾸미기

```python
# 첫번째 줄에 빌딩의 개수 N
# 두번째 줄부터 N+1번째 줄까지(N개의 줄만큼) 각 빌딩의 높이 h가 주어진다.
# 각 빌딩은 오른쪽으로 검사할수 있으며 자기보다 빌딩이 몇개인지 찾아보자

# import sys
# N = int(sys.stdin.readline())
# data = [int(sys.stdin.readline()) for _ in range(N)]
# result = [0]*N
# for i in range(N):
#     for j in range(i+1,N):
#         if data[i] > data[j]:
#             result[i] += 1
#         else:
#             break
# print(sum(result))
# 이중 for문은 시간초과
# 실패, 다른방법으로 해보자
########################################################################

# 풀이
# 1. 스택이 비어있지않고 스택의 마지막값이 비교할 값보다 작으면 계속해서 pop 하는 while
# 2. while 조건에 안걸린다면 stack의 길이를 value에 누적합 하고 현재 빌딩을 스택에 push
# stack의 길이만큼을 누적합 하는 이유 : stack에 남아있는 애들은 현재 검사하는 빌딩(i)를 볼수 있기 때문, 빌딩 i가 하나씩 붙으면 stack에서 보는 애들이 +1 씩 누적합 되는 느낌 (stack에 있는 애들 갯수만큼 계속 더해줌)
# 즉, 얘(i)를 보고있는 빌딩의 갯수가 몇개인지 매번 확인!!

# 입력값 N 6 빌딩(10,3,7,4,12,2)가 주어졌을때
# stack
# 10 (stack의 길이먼저 더한 후에 push 이기 때문에 길이 0, 10을 push)
# 10 3 (10이 볼수있음,길이 1)
# 10 7 (3은 pop하고 나서 계산: 10이 7을 볼수있음,길이 1)
# 10 7 4 ( 10과 7이 4를 볼수 있음,길이 2)
# 12 (12보다 작은값 모두 pop 후에 다시 계산,아무도 12를 볼수없음 길이 0)
# 12 2 (12는 2를 볼수있음, 길이 1)
# 총합 길이 5


import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
value = 0

for i in range(N): # i 는 현재 검사할 빌딩
    while stack and stack[-1] <= data[i]:
        stack.pop()
    value += len(stack)
    stack.append(data[i])

print(value)

```

