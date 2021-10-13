##  1012. 유기농 배추 

```python
# 1012 유기농 배추
# 차세대 영농인 한나.. 한나씨 멋져요
# 배추흰지렁이를 구입하자
# 배추를 군대군대 심어 놓았고, 배추흰지렁이의 총 필요갯수를 구해라
# BOJ 에서는 재귀 깊이르 1000이하로 설정하였고, 이를 해결하기위해 아래와 같은 setrecursionlimit 를 변경해주어 코드를 진행하였따.
import sys

sys.setrecursionlimit(10 ** 6)


# 이 bfs 가 끝나고 나면 visited로 방문할 수 있는 영역은 모두 방문하고, 다음 배추를 찾을 수 있다.
def bfs(y, x):
    visited[y][x] = 1
    # 4 방향으로 돌면서 이동할 수있는 위치가 있는지 확인한다.
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= nx < N and 0 <= ny < M and baechu[ny][nx] and not visited[ny][nx]:
            bfs(ny, nx)
    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    baechu = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        baechu[b][a] = 1
    visited = [[0] * N for _ in range(M)]
    cnt = 0
    # 돌면서 배추는 있는데 칠하진 않은 영역이 있을경우 bfs 로 visited 를 색칠한다. 이후 cnt += 1 을 해주고, 이 값을 출력한다.
    for i in range(M):
        for j in range(N):
            if baechu[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)


```



###  2056. 연월일 달력

```python
# 2056. 연월일 달력
m30 = [4, 6, 9, 11]
m31 = [1, 3, 5, 7, 8, 10, 12]


def solve(arr):
    # 년의 값 y
    y = ''.join(arr[0:4])
    # 달의 값 m
    m = ''.join(arr[4:6])
    # 날의값 d
    d = ''.join(arr[6:8])
    if int(m) in m30 and 1 <= int(d) <= 30:
        return y + '/' + m + '/' + d
    elif int(m) in m31 and 1 <= int(d) <= 31:
        return y + '/' + m + '/' + d
    elif int(m) == 2 and 1 <= int(d) <= 28:
        return y + '/' + m + '/' + d
    else:
        return -1


T = int(input())
for tc in range(1, T + 1):
    ymd = list(input())
    result = solve(ymd)
    print('#{} {}'.format(tc, result))


```



### 5639. 나무 재테크

```python
# 16235. 나무 재테크
# 왤캐 어렵지...
# 우영님은 쉽게풀꺼야 우영님이니까
# 우영님 짱짱..
from collections import deque


def four():
    # 봄에는 나무들이 나이만큼 양분을 먹고 나이가 1 증가한다. 여러개 있으면
    # 나이가 어린 나무들이 양분을 먹고, 늙은애들은 먹지못하고 죽는다.
    for i in range(N):
        for j in range(N):
            # 나무의 갯수
            lt = len(tree[i][j])
            for k in range(lt):
                # 봄에 나무의 나이만큼 양분을 챙겨준다.
                if tree[i][j][k] <= Yang[i][j]:
                    Yang[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    # 여름에 양분을 주지못한 나무들만큼 //2를 하여 양분으로 넣어준다
                    for _ in range(k, lt):
                        Yang[i][j] += tree[i][j].pop() // 2
                    break
    # 가을 진입 가을에는 나무가 8방향으로 자라나게된다.
    for i in range(N):
        for j in range(N):
            lt = len(tree[i][j])
            for k in range(lt):
                # 나무의 나이가 5살일때,
                if tree[i][j][k] % 5 == 0:
                    for dy, dx in [(-1, -1), (0, -1), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, 0)]:
                        ny = dy + i
                        nx = dx + j
                        if 0 <= nx < N and 0 <= ny < N:
                            # 왼쪽에 제일 젊은 나무들을 더해준다.
                            tree[ny][nx].appendleft(1)
            # 겨울 : 나부에 양분을 넣어준다.
            Yang[i][j] += A[i][j]


# 입력부터 보자
# 첫째 쭐에 N, M, K 가 주어진다.
N, M, K = map(int, input().split())
# 둘째 줄에 N개의 줄에 A배열의 값이 주어진다. r 번째 줄에 c번째 값은 A[r][c] 이다.
A = [list(map(int, input().split()))[:N] for _ in range(N)]
# 다음 M 개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x,y,z 가 주어진다.
# 양분이 저장될 이차원 배열 생성
Yang = [[5] * N for _ in range(N)]
# 나무의 위치를 받을 이차원 배열 생성
tree = [[deque() for i in range(N)] for i in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)
for i in range(K):
    # 사계절 함수
    four()
result = 0
for i in range(N):
    for j in range(N):
        # 나무의 갯수를 result 에 넣어준다.
        result += len(tree[i][j])
print(result)

```

### 
