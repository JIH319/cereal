import sys
input = sys.stdin.readline


# 삭제 지점 연결 끊기
def del_n(D):
    for i in range(N):
        if adj[D][i]:
            adj[D][i] = adj[i][D] = 0


# dfs
def cnt_tn(root):
    global cnt
    isTN = True
    visited[root] = 1
    for i in range(N):
        if adj[root][i] and not visited[i]:
            isTN = False
            cnt_tn(i)
    if isTN:
        cnt += 1


N = int(input())
p_list = list(map(int, input().split()))
D = int(input())
# 인접행렬
adj = [[0]*N for _ in range(N)]
for i in range(N):
    if p_list[i] == -1:
        root = i
    else:
        adj[i][p_list[i]] = adj[p_list[i]][i] = 1
cnt = 0
visited = [0]*N
del_n(D)
cnt_tn(root)
if root == D:
    print(0)
else:
    print(cnt)

# 8
# -1 0 0 1 1 2 3 6
# 3

# 12
# 9 2 8 8 -1 3 7 4 4 6 2 6
# 8