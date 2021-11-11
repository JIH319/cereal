# 트리
```python
n = int(input())
arr = list(map(int,input().split()))
remove = int(input())
tree = {}
for i in range(n): # 트리 생성
    if i == remove or arr[i] == remove : # 없애야 될 서브트리는 생성하지 않음
        continue
    if arr[i] in tree.keys(): # 자식이 있으면 key 추가
        tree[arr[i]].append(i)
    else:
        tree[arr[i]]=[i]

print(tree)
check = []
if -1 in tree.keys(): # 루트가 남아 있는지 확인
    check.append(-1)

answer = 0
while check: # 트리를 타고 들어가면서 자식이 없으면(key가 없으면) answer +
    now = check.pop()
    if now not in tree.keys():
        answer +=1
    else:
        check.extend(tree[now])
print(answer)
```

# 공통조상
```python
def find_parent(node):
    parent_list = []
    while True:
        if tree[node][0] == 0 :
            return parent_list
        parent = tree[node][0]
        parent_list.append(parent)
        node = parent


def find_near_node():
    for p1 in node1_parent:
        for p2 in node2_parent:
            if p1 == p2:
                return p1


def find_subtree(node):
    stack = [node]
    cnt = 0
    while stack:
        now_node = stack.pop()
        cnt += 1
        if tree[now_node][1] != 0 :
            stack.append(tree[now_node][1])
        if tree[now_node][2] != 0 :
            stack.append(tree[now_node][2])
    return cnt


for tc in range(1, int(input())+1):
    v, e, node1, node2 = map(int, input().split())
    # 부모, 자식1, 자식2
    tree = [[0, 0, 0] for _ in range(v+1)]
    temp = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        # 부모 - 자식
        tree[temp[i+1]][0] = temp[i]
        if tree[temp[i]][1] == 0:
            tree[temp[i]][1] = temp[i+1]
        else:
            tree[temp[i]][2] = temp[i+1]
    node1_parent = find_parent(node1)
    node2_parent = find_parent(node2)
    near_node = find_near_node()
    print('#{} {} {}'.format(tc, near_node, find_subtree(near_node)))
```
