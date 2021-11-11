# 21736_헌내기는 친구가 필요해
# 대학의 캠퍼스 N X M
# 상하좌우 이동
import sys
from collections import deque

input = sys.stdin.readline


# bfs 로 풀었는데...? 머지
def solve(r, c):
    # 사람만난 횟수를 체크하기 위한 cnt
    cnt = 0
    # 방문한 영역은 1로 표시~ que 는 deque 로 현재 위치를 que 에 삽입
    visited[r][c] = 1
    que = deque([(r, c)])
    # que 가 있는동안 반복문!
    while que:
        rr, cc = que.popleft()
        # 4방향 탐색!
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = rr + dr, cc + dc
            # 캠퍼스 영역을 안벗어나며 벽이아니고, 방문하지 않았으면 들어가는 조건문
            if 0 <= nr < N and 0 <= nc < M and campus[nr][nc] != 'X' and not visited[nr][nc]:
                # 그게 사람이면 cnt +=1 해주자
                if campus[nr][nc] == 'P':
                    cnt += 1
                # 방문했으니 1표시 que 에는 해당 영역 을 append 해주자
                visited[nr][nc] = 1
                que.append((nr, nc))
    return cnt


# [입력]
# 캠퍼스의 크기를 나타내는 두 정수 N 과 M
N, M = map(int, input().split())
# 캠퍼스의 정보 O: 빈 공간, X: 벽, I 는 도연이, P: 사람
campus = [list(input())[:M] for _ in range(N)]
# 시작지점을 받아주고, 찾은 경우 더 볼 필요 없으니 break 해주자
sr, sc = 0, 0
is_valid = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            sr, sc = i, j
            is_valid = 1
            break
    if is_valid:
        break
# 방문 영역을 담기 위한 2차원 배열
visited = [[0] * M for _ in range(N)]
# 반환값을 result 에 넣어주고, 해당 값이 있으면 출력 없으면 'TT' 출력하자
result = solve(sr, sc)
if result:
    print(result)
else:
    print('TT')
