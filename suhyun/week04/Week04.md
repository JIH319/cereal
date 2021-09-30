##  1268. 공통 조상 

```python
# 1248. 공통조상
def pre_order(n):
    global cnt
    if n:  # 유효한 정점이면
        pre_order(t_left[n])
        cnt += 1
        pre_order(t_right[n])


T = int(input())
for tc in range(1, T + 1):
    V, E, V1, V2 = map(int, input().split())
    edge = list(map(int, input().split()))
    t_left = [0] * (V + 1)  # 부모를 인덱스로 자식번호 저장
    t_right = [0] * (V + 1)
    p_list = [0] * (V + 1)
    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]
        if t_left[p] == 0:  # p 의 왼쪽 자식이 없으면
            t_left[p] = c
        else:  # p의 왼족 자식이 있으면 오른쪽 자식으로 저장
            t_right[p] = c
        p_list[c] = p
    # V1 에 대한 조상 리스트
    V1_list = [p_list[V1]]
    while p_list[V1_list[-1]]:
        V1_list.append(p_list[V1_list[-1]])
    # V 에 대한 조상 리스트
    V2_list = [p_list[V2]]
    while p_list[V2_list[-1]]:
        V2_list.append(p_list[V2_list[-1]])
    # 조상 리스트의 교집합 = 공통 조상
    union_list = list(set(V1_list) & set(V2_list))
    min_u = 0
    min_c = 1000000000
    # 공통 조상을 순회하여 가장 최단 거리 순회를 찾으면 min_u 와 min_c 에 대입한다.
    for u in union_list:
        cnt = 0
        pre_order(u)
        if cnt < min_c:
            min_u = u
            min_c = cnt
    print('#{} {} {}'.format(tc, min_u, min_c))


```



###  1068. 트리

```python
# 1068. 트리
# 리프노드를 구하자!
def dfs(e, p):
    p[e] = -10
    for i in range(len(p)):
        if e == p[i]:
            dfs(i, p)


# 노드의 개수 N
N = int(input())
# 노드의 부모 p_list
p_list = list(map(int, input().split()))
# 지울 노드 eraser_node 줄여서 en
en = int(input())
dfs(en, p_list)
cnt = 0
print(p_list)
for i in range(len(p_list)):
    # p_list[i] != -10 : 삭제하여 없어진 노드들을 뜻함.
    # i in p_list: i번째 번호가 p_list 에 있다 = 리프노드가 아니다 란 뜻.
    # 즉, 반대로 생각하여 i번째 번호가 p_list 에도 없다면 리프노드란 뜻이다.
    if p_list[i] != -10 and i not in p_list:
        cnt += 1
print(cnt)


```



### 1855. 영준이의 진짜 BFS

```python
# 1855. 영준이의 진짜 BFS 실패
from collections import deque

# 테스트 케이스의 수 T
T = int(input())
for tc in range(1, T + 1):
    # 노드의 수 N
    N = int(input())
    node_path = [0, 0] + list(map(int, input().split()))
    que = deque()
    for i in range(N):
        for j in range(1, len(node_path)):
            if node_path[j] == i:
                que.append(j)
    result = 0
    for k in range(len(que) - 1):
        V1que = deque()
        V1que.append(que[k])
        while node_path[V1que[-1]]:
            V1que.append(node_path[V1que[-1]])
        V2que = deque()
        V2que.append(que[k + 1])
        while node_path[V2que[-1]]:
            if node_path[V2que[-1]] in V1que:
                while node_path[V2que[-1]]!=V1que.pop():continue
                break
            V2que.append(node_path[V2que[-1]])
        result += len(V1que)+len(V2que)
    print('#{} {}'.format(tc,result))

```



### 5639. 이진 검색 트리

```python
# 5639. 이진 검색 트리
# 노드에 들어있는 키의 값은 106보다 작은 양의 정수
import sys

sys.setrecursionlimit(10 ** 9)


def post_order(s, e):
    if s > e:
        return
    # e+1 이란건, 기존 점위를 벗어난 특정값, 즉 범위에 없는 최대 값을 뜻한다.
    div = e + 1

    for i in range(s + 1, e + 1):
        if tree[s] < tree[i]:
            div = i
            break
    post_order(s + 1, div - 1)  # 왼쪽 트리를 뜻함
    post_order(div, e)  # 오른쪽 트리를 뜻함.
    print(tree[s])  # 오른쪽 -> 루트 -> 왼쪽 순의 후위 순회를 출력함.


tree = []
cnt = 0
# 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하
while cnt <= 10000:
    try:
        num = int(input())
    except:
        break
    tree.append(num)
    cnt += 1
post_order(0, len(tree) - 1)

```

