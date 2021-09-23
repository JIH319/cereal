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
