### 4299. 태혁이의 사랑은 타이밍 - D3
```python
# 불쌍한 태혁이 ㅠ..
def Chim(d, h, m):
    Dt = 11  # 어짜피 다 11이니 통일하자
    rst = (d - Dt) * 24 * 60 + (h - Dt) * 60 + (m - Dt)
    if rst < 0:
        return -1
    return rst


# [ 입 력 ]
# 첫째 줄에는 테스트 케이스의 수가 주어진다.
T = int(input())
for tc in range(1, T + 1):
    # 테스트 케이스 각 줄에는 3개의 정수가 주어진다.
    D, H, M = map(int, input().split())

    # 각각의 케이스마다 각 줄에 태혁이가 얼마나 오랫동안 바람을 맞았는지 분 단위로 출력한다
    # 태혁이가 소개팅 약속시간 전에 차였다면 놀리기엔 너무 불쌍하므로 -1을 출력한다.
    # 재혁이의 소개팅 약속 시간 2011년 11월 11일 오전 11시 11분

    # 차인 분 확인하기 위한 함수 불러오기
    result = Chim(D, H, M)
    print('#{} {}'.format(tc, result))
```



### 2589. 보물을 찾자. Gold 5

```python
# 첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다.
from collections import deque # pop은 메모리가 많이먹는자는 지은신의 말을 빌어 처음 사용했음


def my_max(a, b): # max 값을 찾기 위한 자체 제작
    if a > b:
        return a
    return b


def bfs(x, y): # bfs 를 돌리기 위한 제작
    que = deque()  # que 는 deque 라고 선언해준다.
    que.append([x, y])  # que 에 시작 위치 x, y를 할당하고 시작한다.
    cnt = 0  # 나중에 최단거리를 반환하기 위한 int 형
    while que: # que 를 다 쓸 때 까지, 즉, 갈 수 있는 최종 거리까지 도달한지 확인한다.
        cx, cy = que.popleft() # 현재 위치에 대한 값을 받아준다.
        for k in ([1, 0], [-1, 0], [0, -1], [0, 1]):  # 4가지 방향으로 다 돌려서 갈 수 있으면 +1 해주며 앞으로 나아간다.
            nx = cx + k[0]
            ny = cy + k[1]
            if 0 <= nx < xx and 0 <= ny < yy and visited[nx][ny] == 0 and island[nx][ny] != 'W':
                visited[nx][ny] = 1 # 방문가능한 영역인경우, 방문했다는 표시를 해주고,
                island[nx][ny]=island[cx][cy]+1 # 그 진행한 시간을 기록해준다.
                cnt = island[nx][ny]
                que.append([nx, ny]) # 이 영역으로 진행 했으므로, 이값을 que에 저장해준다.
    return cnt # 최종적으로 가장 먼 거리까지 이동한 시간을 반환해준다.


xx, yy = map(int, input().split())
island = [list(input()) for _ in range(xx)]
result = 0
for i in range(xx):
    for j in range(yy):
        if island[i][j] != 'W':  # 즉 갈 수 있는 경로인 W일 경우, 갈 수 있는 영역인 경우, 거리를 측정한다.
            visited = [[0] * yy for _ in range(xx)]
            visited[i][j] = 1  # 첫 방준점이므로 1 을 넣어준다.
            island[i][j] = 0  # 첫 시작이므로 0을 넣어준다.
            result = my_max(result, bfs(i, j)) # my_max 를 통해 그 전 값들과 값을 비교하여 최장거리 시간을 측정한다.
print(result)
```



+ 태혁이의 사랑을 응원합니다

+ 태혁아 너두 할 수 있어!