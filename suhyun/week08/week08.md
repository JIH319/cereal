### 2003. 수들의 합 2 (Backjoon)

```python
# 2003.  수들의 합 2
# N개의 수로 된 수열이 있다. 이 수열의 i번째 수부터 j번째 수 까지의 합이 M이 되는 경우의 수를 구하는
# 프로그램을 작성하시오.


def solve():
    global cnt
    for i in range(N):
        # 시작점 i 번째를 둔다.
        cnt_sum = 0
        for j in range(i, N):
            # cnt_sum 에 그 값을 더해준 후에 조건문을 판별한다.
            cnt_sum += arr[j]
            # 넘어설경우 더 볼필요 없다 break 해준다.
            if cnt_sum > M:
                break
            # 일치한 경우, count 를 올려주고 break 해준다.
            if cnt_sum == M:
                cnt += 1
                break
            # 미 일치시, continue 로 다음 j 번째 수를 더해준다.
            else:
                continue


# 입력
N, M = map(int, input().split())  # N : 수열의 수, M : 구해야하는 경우의 수
arr = list(map(int, input().split()))  # 수열이 가지고 있는 수
# 비트연산으로 구해보자
cnt = 0
solve()
print(cnt)

```



### 3176. 도로 네트워크(Backjoon)

```python
```





### 1949. 등산로 조성(SWEA)

```python
# 1949. 등산로 조성
# 등산로는 가장 높은 봉우리에서 시작해야 한다.
# 산으로 올라갈수 있도록 높은 지형에서 낮은 지역으로 가로 또는 세로 방향으로 연결이 되야한다.
# 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능 하다.
# 긴 등상로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
# N*N 크키의 지도가 주어지고, 최대 공사 가능깊이 K 가 주어진다.


# 1. 현재 위치를 들고 다니지 않을 때
# r,c 좌표, road 는 지금까지 조성된 등산로의 길이, skill 은 공사 유무 확인
def work(r, c, road, k):
    global rst
    if road > rst:
        rst = road
    visited[r][c] = 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # a. 현 위치보다 낮은 곳을 이동할 때에는,
            if arr[r][c] > arr[nr][nc]:
                work(nr, nc, road + 1, k)
            # b. 현 위치보다 높거나 같은 곳으로 이동할 때에는, (위에가 맞다면, 무조건 따르는게 문제 내에서 좋기 때문에)
            elif k and arr[r][c] > arr[nr][nc] - K:
                # 기존의 값을 저장한 뒤에, 땅 다지기 스킬을 사용하여, 재귀한다.
                tmp = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                work(nr, nc, road + 1, 0)  # 스킬 사용
                arr[nr][nc] = tmp  # 원상 복구
    # 사용을 완료한 후 , 다음 등상로를 확인하기 위해 초기화 해준다.
    visited[r][c] = 0


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 한변의 길이, K: 최대 공사 깊이
    arr = [list(map(int, input().split())) for _ in range(N)]  # 등산로 배열을 받은 것.
    max_h = 0  # 높이는 1~ 20까지 주어지므로, 해당 하는 값에 해당 하지 않는 가장 최소값으로 준다.
    # 확인해야할 좌표를 받을 list 생성
    xy = []
    for i in range(N):
        for j in range(N):
            # 가장 높은 봉우리의 값을 찾아 낸다.
            if max_h < arr[i][j]:
                max_h = arr[i][j]
                xy = [(i, j)]
            # 가장 높은 봉우리의 좌표를 append 해준다.
            elif max_h == arr[i][j]:
                xy.append((i, j))
    visited = [[0] * N for _ in range(N)]

    rst = 0
    for x, y in xy:
        work(x, y, 1, 1)  # 좌표, 길, 스킬

    print('#{} {}'.format(tc, rst))

```

