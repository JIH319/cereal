# 시간 초과;;

import sys
input = sys.stdin.readline


# 파이프의 뒤쪽은 앞쪽이 이동하면 그 자리로 오기 때문에
# 앞쪽 파이프만 이동가능한지 조사
# 파이프가 (N-1, N-1)으로 갈 수 있는 경우의 수를 구하기
def dfs(pre, cur): # cur: 파이프의 앞쪽(나아가는 쪽)의 행과 열
    global cnt
    pi, pj = pre
    ci, cj = cur
    if ci == N - 1 and cj == N - 1:
        cnt += 1
        return
    # 지금 파이프가 가론지 세론지 대각선인지 알아야 함
    if pi == ci:
        d = [(0, 1), (1, 1)] # 가로
    elif pj == cj:
        d = [(1, 0), (1, 1)] # 세로
    else:
        d = [(0, 1), (1, 0), (1, 1)] # 대각선
    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
            if di == 1 and dj == 1: # 대각선으로 움직인다면 3방향 확인
                if not arr[ci+1][cj] and not arr[ci][cj+1]:
                    dfs(cur, (ni, nj))
            else:   # 대각선으로 움직이는게 아니라면
                dfs(cur, (ni, nj))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs((0, 0), (0, 1))
print(cnt)
