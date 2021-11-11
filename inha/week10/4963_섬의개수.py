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