# 1. DFS
def dfs(idx):
    # 현재 노드 위치에서 방문처리 해주고, 방문한 순서대로 print
    visited[idx] = 1
    print(idx, end=' ')
    # 현재 노드와 연결 되어있는 노드들 순서대로!
    for i in arr[idx]:
        # 방문하지 않앗으면 재귀 함수 호출
        if not visited[i]:
            dfs(i)

# 2. BFS
def bfs(idx):
    # 현재 노드 위치에서 방문처리 해주고, q에 append
    visited2[idx] = 1
    q = deque()
    q.append(idx)

    # q가 비지 않는 동안
    while q:
        # 현재 노드 위치를 now로 잡고, print()
        now = q.popleft()
        print(now, end=' ')

        # 현재 노드 위치와 연결되어있는 노드들을 순서대로 확인해서, 방문 안했다면 방문처리하고 q에 넣기
        for i in arr[now]:
            if visited2[i] == 0:
                visited2[i] = 1
                q.append(i)
        # 만약 q에 넣지 못할 경우 다시 while 처음으로 돌아가고, q가 비면 함수 끝


from collections import deque
N, M, V = map(int, input().split())
# 각 노드가 어떻게 연결 되어 있는지 그래프로 나타내기
arr = [[] for _ in range(N+1)]
for n in range(M):
    a, b = map(int, input().split())
    # 노드끼리 서로 연결하고, 숫자 낮은순서대로 넣기 때문에 sort() 필수
    arr[a].append(b)
    arr[a].sort()
    arr[b].append(a)
    arr[b].sort()
visited = [0] * (N+1)
dfs(V)
visited2 = [0] * (N+1)
print()
bfs(V)
