### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="20" height="20">[[1260]DFS와 BFS](https://www.acmicpc.net/problem/1260)

```python
import sys
from collections import deque
input = sys.stdin.readline
# DFS로 탐색한 결과와 BFS로 탐색한 결과 출력
# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
# 정점 번호는 1~N
def dfs(start):
    stack = [start]
    print(start, end=' ')
    visited = [0] * (N+1)
    visited[start] = 1
    while stack:
        cur = stack[-1]
        for next_n in adj_lst[cur]:
            # next_n 이 0이면(방문하지 않았으면)
            if not visited[next_n]:
                print(next_n, end=' ')
                stack.append(next_n)
                visited[next_n] = 1 # 방문표시
                break
        else:
            stack.pop()


def bfs(start):
    q = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1

    while q:
        # 큐에서 뺄때 해당 노드 print
        cur = q[0]
        print(cur, end=' ')
        # cur 노드와 연결된 모든 노드를 q에 저장
        for next_n in adj_lst[cur]:
            if not visited[next_n]:
                q.append(next_n)
                visited[next_n] = 1 # 방문 표시
        # q에 가장 첫번째 요소 pop
        q.popleft()


N, M, V = map(int, input().split())
# 인접 리스트
adj_lst = [[] for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    # 양방향 노드
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문하므로
for lst in adj_lst:
    lst.sort()

dfs(V)
print()
bfs(V)
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="20" height="20">[[21736]헌내기는 친구가 필요해](https://www.acmicpc.net/problem/21736)

```python
import sys
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    cnt = 0
    arr[start[0]][start[1]] = 'X'    # 방문표시
    while stack:
        ci, cj = stack[-1]
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'X':
                # 'P'이면 cnt +1
                if arr[ni][nj] == 'P':
                    cnt += 1
                arr[ni][nj] = 'X'    # 방문표시
                stack.append((ni, nj))
                break
        else:
            stack.pop()
    # cnt가 0일 경우 'TT' return
    if cnt:
        return cnt
    else:
        return 'TT'


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

# 도연이 위치 찾기
start = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            start = (i, j)
            break
    if start:
        break

print(dfs(start))
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" width="20" height="20"><img src="https://d2gd6pc034wcta.cloudfront.net/tier/7.svg" width="20" height="20">[[1388]바닥장식](https://www.acmicpc.net/problem/1388)

```python
import sys
input = sys.stdin.readline

# 바닥 장식 몇개 필요한지 체크하는 함수
def check(arr, match):
    cnt = 0
    # 직사각형 arr의 행만큼 돔
    for i in range(len(arr)):
        # 다음 행으로 넘어갈때마다 isMatch를 False로 초기화
        isMatch = False
        # 직사각형 arr의 열만큼 돔
        for j in range(len(arr[0])):
            # isMatch가 False이면서 arr[i][j]가 찾는 문자와 똑같은 경우 cnt + 1
            # (즉, match 문자가 연속으로 올 때는 cnt +1을 해주지 않음)
            if not isMatch and arr[i][j] == match:
                isMatch = True
                cnt += 1
            # match 문자와 다른 문자가 올 경우 isMatch는 False
            elif arr[i][j] != match:
                isMatch = False
    return cnt


N, M = map(int, input().split())
floor1 = [list(input().rstrip()) for _ in range(N)]
# '|'문자는 같은 열에 있는 것을 찾아야 하므로 check함수에 적용시키기 위해 전치행렬 만듦
floor2 = [[] for _ in range(M)]
for j in range(M):
    for i in range(N):
        floor2[j].append(floor1[i][j])

print(check(floor1, '-')+check(floor2, '|'))
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/9.svg" width="20" height="20">[[4963]섬의개수](https://www.acmicpc.net/problem/4963)

```python
import sys
input = sys.stdin.readline
# 섬의 개수를 세는 프로그램
# 8방, 시계방향
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def dfs(si, sj):
    stack = [(si, sj)]
    arr[si][sj] = 0
    while stack:
        ci, cj = stack[-1]
        for di, dj in dir:
            ni, nj = ci + di, cj +dj
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj]:
                stack.append((ni, nj))
                arr[ni][nj] = 0
                break
        else:
            stack.pop()


while True:
    w, h = map(int, input().split())
    # 종료 조건
    if w == 0 and h == 0:
        break
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(h)]
    # 지도 arr을 돌면서 땅인 곳이 나오면 그 곳을 시작점으로 dfs 함수 실행
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                # dfs 돌면서 시작점 (i, j)에서 갈 수 있는 모든 땅(1)을 0으로 바꿔줌
                dfs(i, j)
                cnt += 1
    print(cnt)
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/8.svg" width="20" height="20">[[2606]바이러스](https://www.acmicpc.net/problem/2606)

```python
import sys
input = sys.stdin.readline
# 네트워크상 연결된 컴퓨터들 중 하나라도 바이러스 걸리면 다 걸림
# 1번 컴퓨터가 바이러스에 걸렸을 때 바이러스에 걸리는 컴퓨터의 수
def dfs():
    cnt = 0
    # 1번 노드부터 시작
    stack = [1]
    visited = [0] * (N+1)
    visited[1] = 1  # 방문표시
    while stack:
        cur = stack[-1]
        for next_n in adj_lst[cur]:
            if not visited[next_n]:
                stack.append(next_n)
                visited[next_n] = 1 # 방문표시
                cnt += 1
                break
        else:
            stack.pop()
    return cnt


N = int(input())
E = int(input())
# 인접 리스트
adj_lst = [[] for _ in range(N+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    # 양방향
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

print(dfs())


```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" width="20" height="20">[[2493]탑](https://www.acmicpc.net/problem/2493)

```python
# 오큰수랑 푸는 방법 똑같,,
import sys
input = sys.stdin.readline
# 일직선 위에 N개의 높이가 서로 다른 탑 꼭대기에 송신기
# 왼쪽으로 송신
N = int(input())
heights = list(map(int, input().split()))

stack = [N-1]
ans = [0] * N

# 거꾸로
for i in range(N-2, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        ans[stack.pop()]= i+1
    stack.append()

print(*ans)
```



### <img src="https://d2gd6pc034wcta.cloudfront.net/tier/11.svg" width="20" height="20">[[6198]옥상정원꾸미기](https://www.acmicpc.net/problem/6198)

```python
# 이것도 오큰수 비슷..!
import sys
input = sys.stdin.readline

N = int(input())
buildings = []
for _ in range(N):
    h = int(input())
    buildings.append(h)
# 빌딩 최고 높이가 1000000000
# 마지막에 최고 높이의 빌딩이 있다고 가정
buildings.append(1000000000)

# 인덱스 0 부터 시작
stack = [0]
# 합계 저장할 변수
result = 0

idx = 0
# 마지막 임의로 추가한 빌딩까지 N개이므로 range(1, N+1)
for i in range(1, N+1):
    # 자기 높이보다 낮은 빌딩 개수를 찾아야함
    # 자기보다 높거나 같은 빌딩이 오면 stack에서 pop하고 그 값을 idx에 저잘
    while stack and buildings[stack[-1]] <= buildings[i]:
        idx = stack.pop()
        # idx번째 빌딩은 idx+1부터 i-1번째까진 모두 자기보다 낮은 빌딩이었음
        # 따라서 합계를 저장하는 result에 (i-idx)-1을 더함
        result += (i - idx) - 1
    # 자기보다 낮은 빌딩이 오면 stack에 append
    stack.append(i)

print(result)
```

