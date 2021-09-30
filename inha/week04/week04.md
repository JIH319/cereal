### [SWEA/1248] 공통조상

```python
def find_parent(child, c_parent):
    if parent[child]:
        c_parent.append(parent[child])
        find_parent(parent[child], c_parent)


def find_cp(c1_p, c2_p):
    for p1 in c1_p:
        for p2 in c2_p:
            if p1 == p2:
                return p1


def subtree(start):
    global sub_cnt
    if left[start]:
        sub_cnt += 1
        subtree(left[start])
    if right[start]:
        sub_cnt += 1
        subtree(right[start])


T = int(input())
for tc in range(1, T+1):
    V, E, c1, c2 = map(int, input().split())
    left = [0]*(V+1)
    right = [0]*(V+1)
    parent = [0]*(V+1)
    edge = list(map(int, input().split()))
    for i in range(0, E*2-1, 2):
        p, c = edge[i], edge[i+1]
        if not left[p]:
            left[p] = c
        else:
            right[p] = c
        parent[c] = p
    c1_parent = []
    c2_parent = []
    find_parent(c1, c1_parent)
    find_parent(c2, c2_parent)
    cp = find_cp(c1_parent, c2_parent)
    sub_cnt = 0
    subtree(cp)
    print('#{} {} {}'.format(tc, cp, sub_cnt+1))
```



### [백준/1068] 트리

```python
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
```

