# 첫째줄 컴퓨터의 수 N
# 컴퓨터는 1번부터 번호가 매겨진다.
# 둘째줄에는 연결되어있는 컴퓨터의 쌍 수가 주어진다.
# 세번째 줄부터는 컴퓨터의 쌍 수 만큼 연결되어있는 컴퓨터 번호 쌍이 주어진다.

# 1번 컴퓨터가 바이러스 걸렸을때 1번컴퓨터와 연결되어있는 컴퓨터의 수를 출력하라
# bfs로도 풀수 있지만 dfs로 queue에 값이 들어갈때마다 카운트 해보자


def dfs(v):
    global ans
    visited[v] = 1
    for i in range(1,N+1):
        # v는 현재 컴퓨터 번호, v와 연결된 컴퓨터가 있는지 i로 검사한다.
        if computers[v][i] and not visited[i]:
            ans += 1
            dfs(i)



N = int(input())
M = int(input())
# 배열의 각 행의 순서를 컴퓨터 번호로 인식하기 위해 가로세로 N+1 만큼의 배열을 생성해준다.
computers = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):  # M개의 쌍을 만들어 놓은 computers 배열에 넣는다.(1 체크)
    com1,com2 = map(int,input().split())
    computers[com1][com2] = 1
    computers[com2][com1] = 1
visited = [0]*(N+1) # 방문체크할 배열
ans = 0
dfs(1)
print(ans)
