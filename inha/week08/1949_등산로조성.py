def dfs(r, c, chance):
    global MAX, visited
    MAX = max(MAX, visited[r][c])
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
        if arr[r][c] > arr[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance)
            visited[nr][nc] = 0
        elif chance and arr[nr][nc] - K < arr[r][c]:
            temp = arr[nr][nc]
            arr[nr][nc] = arr[r][c] - 1
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance-1)
            visited[nr][nc] = 0
            arr[nr][nc] = temp


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = []
    top = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            if arr[i][j] > top:
                top = arr[i][j]
    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print("#{} {}".format(tc, MAX))