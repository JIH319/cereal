import sys
from collections import deque
input = sys.stdin.readline
# DFS로 탐색한 결과와 BFS로 탐색한 결과 출력
# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
# 정점 번호는 1~N
def dfs(start):
    stack = [start]
    print(start, end=' ')
    visited = [0] * (N+1)
    visited[start] = 1
    while stack:
        cur = stack[-1]
        for next_n in adj_lst[cur]:
            # next_n 이 0이면(방문하지 않았으면)
            if not visited[next_n]:
                print(next_n, end=' ')
                stack.append(next_n)
                visited[next_n] = 1 # 방문표시
                break
        else:
            stack.pop()


def bfs(start):
    q = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1

    while q:
        # 큐에서 뺄때 해당 노드 print
        cur = q[0]
        print(cur, end=' ')
        # cur 노드와 연결된 모든 노드를 q에 저장
        for next_n in adj_lst[cur]:
            if not visited[next_n]:
                q.append(next_n)
                visited[next_n] = 1 # 방문 표시
        # q에 가장 첫번째 요소 pop
        q.popleft()


N, M, V = map(int, input().split())
# 인접 리스트
adj_lst = [[] for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    # 양방향 노드
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문하므로
for lst in adj_lst:
    lst.sort()

dfs(V)
print()
bfs(V)


