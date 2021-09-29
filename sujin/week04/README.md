### 1248_공통조상

```python
# 공통 조상 찾기
def find(N1,N2):
    q = [N1,N2]
    visited = [0]* (V+1)
    while q:
        current = q.pop(0)
        # 부모노드가 있고(루트 아님)
        if tree[current]:
            # 해당 부모노드 방문한적 없으면
            if not visited[tree[current]]:
                q.append(tree[current])
                visited[tree[current]] = 1
            else:
                return tree[current]

# 서브트리 크기 구하기
def dfs(start):
    visited = [0] * (V+1)
    visited[start] = 1
    stack = [start]
    # cnt : 서브 트리의 크기, 루트 제외
    cnt = 1
    while stack:
        temp = stack[-1]
        for i in range(2,V+1):
            # 현재 노드의 자식노드를 스택에 담기
            if tree[i] == temp and not visited[i]:
                stack.append(i)
                visited[i] = 1
                cnt += 1
                break
        else:
            stack.pop()
    return cnt

for tc in range(1,int(input())+1):
    V, E, N1, N2 = map(int,input().split())
    data = list(map(int,input().split()))
    tree = [0] * (V+1)
    for i in range(E):
        # tree의 인덱스 : 자식노드, value: 부모노드
        tree[data[2*i +1]] = data[2*i]

    root = find(N1,N2)
    result = dfs(root)
    print('#{} {} {}'.format(tc,root,result))
```





### 1068_bkj_트리

```python
import sys


def delete_node(target):
    # 루트 지울거면 단말노드 개수 0 반환
    if tree[target] == -1:
        return 0

    # 부모노드가 없게끔한다 >> 트리 연결 사라진 효과
    tree[target] = -2
    stack = [target]

    # 지워야할 노드들을 담을 스택
    while stack:
        current = stack.pop()
        if current in tree: # 현재 노드를 부모로 하는 노드가 있으면 반복
            for j in range(N):
                # 지우려는 노드를 부모로 하는 자식노드도 모두 부모노드 없앤다 >> 트리연결 사라진 효과
                if current == tree[j]:
                    stack.append(j)
                    tree[j] = -2

    cnt = 0
    for i in range(N):
        # 부모노드가 없거나(루트 or 트리에서 제거) 
        # 본인을 부모로 하는 노드가 있다면 >> 단말노드 아님
        if tree[i] == -1 or tree[i] == -2 or i in tree:
            continue
        # 단말노드
        else:
            cnt += 1

    return cnt

N = int(sys.stdin.readline().rstrip())
# 인덱스 : 자식노드 , 값 : 부모노드
tree = list(map(int,sys.stdin.readline().split()))
# 지울 노드의 번호 
target = int(sys.stdin.readline().rstrip())

cnt = delete_node(target)

# 단말노드가 없는데, 제거한 노드가 루트가 아니라면
# 단말 노드 1개 >> 루트
if not cnt and tree[target] != -1:
    print(1)
else:
    print(cnt)
                
```

