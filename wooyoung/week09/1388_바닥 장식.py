def dfs(r,c):
    # 현재 나의 위치 방문처리 해주기
    visited[r][c] = 1
    # 현재 내가 위치한 타일이 '-'인 경우
    if arr[r][c] == '-':
        # 오른쪽 타일(다음 열)이 범위 벗어나지 않고, 방문하지 않았고, - 인 경우 해당 타일로 재귀함수 ㄱㄱ
        if 0 <= c+1 < M and not visited[r][c+1] and arr[r][c+1] == '-':
            dfs(r, c+1)
    # 현재 내가 위치한 타일이 "|"인 경우
    if arr[r][c] == '|':
        # 밑의 (다음 행) 타일이 범위 벗어나지 않고, 방문하지 않았고, |인 경우 해당 타일로 재귀함수 ㄱ ㄱ
        if 0 <= r + 1 < N and not visited[r+1][c] and arr[r+1][c] == '|':
            dfs(r+1, c)


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
# 같은 타일 확인하면 안되기 때문에 방문처리 필수
visited = [[0] * M for _ in range(N)]
cnt = 0
# 모든 바닥 확인하기
for i in range(N):
    for j in range(M):
        # 방문하지 않은 바닥이면 dfs 함수 발동!
        if not visited[i][j]:
            dfs(i,j)
            # 이어져있는 타일 돌고 왔기 때문에 함수가 끝나면 타일 + 1
            cnt += 1

print(cnt)