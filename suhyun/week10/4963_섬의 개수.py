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