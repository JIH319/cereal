import sys
input = sys.stdin.readline


def dfs(cur, dir):
    global cnt
    ci, cj = cur
    if ci == N - 1 and cj == N - 1:
        cnt += 1
        return
    if 0 <= ci+1 < N and 0 <= cj+1 < N and not arr[ci+1][cj] and not arr[ci][cj+1] and not arr[ci+1][cj+1]:
        dfs((ci+1, cj+1), 2)
    if dir == 0 or dir == 2: # 가로 또는 대각선
        if 0 <= cj+1 < N and not arr[ci][cj+1]:
            dfs((ci, cj+1), 0)
    if dir == 1 or dir == 2: # 세로 또는 대각선
        if 0 <= ci+1 < N and not arr[ci+1][cj]:
            dfs((ci+1, cj), 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs((0, 1), 0)
print(cnt)
