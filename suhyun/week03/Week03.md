##  10814.나이 순 정렬 

```python
# 10814_나이 순 정렬
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로,
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오

import sys

input = sys.stdin.readline
# [입력]
# 첫째 줄에 온라인 저지회원의 수 N이 주어진다.(1<=N<=100,000)
N = int(input())
# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다.
# 나이는 1보다 크거나 같으며,200보다 작거나 같은 정수이고,이름은알파벳 대소문자로 이루어져있고,
# 길이가 100보다 작거나 같은 문자열이다.
oja = []
for n in range(N):
    # 온라인 저지 회원의 수 (Online Judge Account)
    #     oja.append([n]+input().split())
    #     oja[n][1] = int(oja[n][1])
    #     for j in range(n):
    #         if oja[n][1]<oja[j][1]:
    #             oja[n],oja[j]=oja[j],oja[n]
    #         elif oja[n][1]==oja[j][1]:
    #             if oja[n][0]<oja[j][0]:
    #                 oja[n], oja[j] = oja[j], oja[n]
    # for i in range(N):
    #     print('{} {}'.format(oja[i][1],oja[i][2]))
    oja.append(input().split())
    oja[n][0] = int(oja[n][0])
oja.sort(key=lambda x: x[0])
for i in range(N):
    print('{} {}'.format(oja[i][0], oja[i][1]))

```



###  4223. 삼성이의 트라우마 극복

```python
# 4223. 삼성이의 트라우마 극복
# 테스트 케이스의 수 T
T = int(input())
for tc in range(1,T+1):
    # 면접관 수 N
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(n+1)
    # 면접관 정리
    mj = []
    for _ in range(N):
        # 면접관에 더해주쟈.
        mj.append([int(input()), list(input().split()), int(input())])
    # SAMSUNG
    min_sum = 10000
    n = len(arr)
    for i in range(1 << n):
        rst = {'S': 0, 'A': 0, 'M': 0, 'U': 0, 'N': 0, 'G': 0}
        m_sum = 0
        for j in range(n):
            if i & (1 << j):
                for a in mj[j][1]:
                    if not rst.get(a) is None:
                        rst[a] += 1
                m_sum += mj[j][2]
        if rst['S'] >= 2 and rst['A'] and rst['M'] and rst['U'] and rst['N'] and rst['G']:
            if min_sum > m_sum:
                min_sum = m_sum
    if min_sum == 10000:
        min_sum = -1
    print('#{} {}'.format(tc, min_sum))
```



### 2667. 단지번호 붙이기

```python
# 2667. 단지번호 붙이기
# [입력]
# 첫번째 줄에는 지도의 크기 N이 입력되고, 그 다음 N 줄에는 각각 N개의 자료(0혹은 1)가 입력된다.\
from collections import deque


def bfs(x, y):  # bfs 를 돌리기 위한 제작
    que = deque()  # que 는 deque 라고 선언해준다.
    que.append([x, y])  # que 에 시작 위치 x, y를 할당하고 시작한다.
    visited[x][y]=cnt
    while que:  # que 를 다 쓸 때 까지, 즉, 갈 수 있는 최종 거리까지 도달한지 확인한다.
        cx, cy = que.popleft()  # 현재 위치에 대한 값을 받아준다.
        for k in ([1, 0], [-1, 0], [0, -1], [0, 1]):  # 4가지 방향으로 다 돌려서 갈 수 있으면 +1 해주며 앞으로 나아간다.
            nx = cx + k[0]
            ny = cy + k[1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                visited[nx][ny] = cnt  # 방문가능한 영역인경우, 방문했다는 표시를 해주고,
                que.append([nx, ny])  # 이 영역으로 진행 했으므로, 이값을 que에 저장해준다.


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

# 총 단지 수 출력
print(cnt - 1)
# 결과를 나중에 오름차순 정렬하기 위해 리스트 호출
result = []
# cnt 만큼 도는 반복문.
for k in range(1, cnt):
    rst = 0
    # 열마다 cnt 가몇개있는지 더해서 합쳐준다.
    for n in range(N):
        if visited[n].count(k):
            rst += visited[n].count(k)
        else:
            continue
    # 모든 값을 더해준후 리스트에 추가해준다.
    result.append(rst)
# 구한 값들을정렬한 후 출력해준다.
result.sort()
for r in result:
    print(r)


```

