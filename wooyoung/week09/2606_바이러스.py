def dfs(idx):
    global cnt
    visited[idx] = 1

    for k in arr[idx]:
        if not visited[k]:
            cnt += 1
            dfs(k)

N = int(input())
V = int(input())
arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

# 연결관계 그래프 그리기
for _ in range(V):
    i, j = map(int, input().split())
    arr[i].append(j)
    arr[i].sort()
    arr[j].append(i)
    arr[j].sort()
dfs(1)
print(cnt)