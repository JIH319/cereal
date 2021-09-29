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