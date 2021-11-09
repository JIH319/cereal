import sys
input = sys.stdin.readline
# 네트워크상 연결된 컴퓨터들 중 하나라도 바이러스 걸리면 다 걸림
# 1번 컴퓨터가 바이러스에 걸렸을 때 바이러스에 걸리는 컴퓨터의 수
def dfs():
    cnt = 0
    # 1번 노드부터 시작
    stack = [1]
    visited = [0] * (N+1)
    visited[1] = 1  # 방문표시
    while stack:
        cur = stack[-1]
        for next_n in adj_lst[cur]:
            if not visited[next_n]:
                stack.append(next_n)
                visited[next_n] = 1 # 방문표시
                cnt += 1
                break
        else:
            stack.pop()
    return cnt


N = int(input())
E = int(input())
# 인접 리스트
adj_lst = [[] for _ in range(N+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    # 양방향
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

print(dfs())

