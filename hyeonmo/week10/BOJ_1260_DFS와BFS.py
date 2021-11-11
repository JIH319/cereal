# DFS와 BFS로 탐색한 결과를 각각 출력
# 방문가능한곳이 한번에 여러곳이라면 가장 작은번호 먼저 방문
# 방문할수 있는곳이 없은경우 종료
# 정점 번호는 1번부터 N번 까지

# 첫째줄에 정점개수 N 간선개수 M 시작할 정점번호 V
# 이후 M개의 줄에 연결되어있는 두개의 정점번호 주어짐

from collections import deque

def dfs(v):
    result_dfs.append(v)
    visited[v] = 1
    for i in range(1,N+1):
        if arr[v][i] and not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        front = queue.popleft()
        result_bfs.append(front)
        for i in range(1,N+1):
            if arr[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1




N,M,V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    r,c = map(int,input().split())
    arr[r][c] = 1
    arr[c][r] = 1
visited = [0]*(N+1)
result_dfs = []
result_bfs = []
dfs(V)
print(*result_dfs)

visited = [0]*(N+1)
bfs(V)
print(*result_bfs)