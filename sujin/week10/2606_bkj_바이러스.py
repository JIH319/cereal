#  한 컴퓨터가 웜 바이러스에 걸리면
#  그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스
# while 반복버전
def dfs():
    # 1번부터 출발하여 갈 수 있는 모든 점 세기
    cnt = 0
    stack = [1]
    visited = [0]*(N+1)
    visited[1] = 1

    while stack:
        cur = stack[-1]
        for i in range(1,N+1):
            # 방문 가능, 미방문
            if adj[cur][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                cnt += 1
                break
        else:
            stack.pop()
    print(cnt)

# 재귀 버전
def dfs_recursion(current):
    global count
    selected[current] = 1
    for i in range(1, N+1):
        # 방문가능, 미방문
        if adj[current][i] and not selected[i]:
            count += 1
            dfs_recursion(i)

# N: 컴퓨터의 수 (1번부터 N번까지), M : 연결 쌍의 수 
N = int(input())
M = int(input())

adj= [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    adj[s][e] = 1
    adj[e][s] = 1

dfs()

count = 0
selected = [0]*(N+1)
dfs_recursion(1)
print(count)