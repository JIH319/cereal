import sys
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    cnt = 0
    arr[start[0]][start[1]] = 'X'    # 방문표시
    while stack:
        ci, cj = stack[-1]
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'X':
                # 'P'이면 cnt +1
                if arr[ni][nj] == 'P':
                    cnt += 1
                arr[ni][nj] = 'X'    # 방문표시
                stack.append((ni, nj))
                break
        else:
            stack.pop()
    # cnt가 0일 경우 'TT' return
    if cnt:
        return cnt
    else:
        return 'TT'


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

# 도연이 위치 찾기
start = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            start = (i, j)
            break
    if start:
        break

print(dfs(start))