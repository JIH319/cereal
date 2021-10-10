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
