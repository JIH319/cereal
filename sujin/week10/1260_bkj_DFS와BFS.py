# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과출력
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문 
# 더 이상 방문할 수 있는 점이 없는 경우 종료 
# 정점 번호는 1번부터 N번까지
# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V

def dfs(start):
    stack = [start]
    visited = [0]*(N+1)
    visited[start] = 1
    print(start,end=' ')
    while stack:
        cur = stack[-1]
        for i in range(1,N+1):
            # 현재 점에서 갈 수 있고, 미방문인 노드 찾으면 >> break
            # 갈 수 있으면 계속 ㄱㄱ
            if adj[cur][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                print(i,end=' ')
                break
        # 갈 수 있는 노드 없음 >> 직전 갈림길로 가서 다른 길 탐색
        else:
            stack.pop()

def dfs_recursion(current):
    selected[current] = 1
    print(current,end=' ')
    for i in range(1,N+1):
        if adj[current][i] and not selected[i]:
            dfs_recursion(i)


def bfs(start):
    q = [start]
    visited = [0]*(N+1)
    visited[start] = 1
    print(start,end=' ')

    while q:
        cur = q.pop(0)
        for i in range(1,N+1):
            # 방문 가능, 미방문 >> 현재 위치에서 갈 수 있으면 다 담기
            if adj[cur][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                print(i,end=' ')

N,M,V = map(int,input().split())
# 두 정점 사이 간선 여러개 있을 수 있음 & 양방향
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    adj[s][e] = 1
    adj[e][s] = 1

selected=[0]*(N+1)
dfs_recursion(V)
# dfs(V)
print()
bfs(V)
