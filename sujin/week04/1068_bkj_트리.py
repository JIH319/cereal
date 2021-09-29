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


                    