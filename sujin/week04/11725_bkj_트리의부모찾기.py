import sys

N = int(sys.stdin.readline().rstrip())
# 트리 초기설정
tree = [0] * (N+1)
tree[1] = -1 # 루트 부모노드 없음 설정

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    # a노드 부모노드 있으면 >>  a : 부모노드, b : 자식노드 
    if tree[a]:
        tree[b] = a
    else:
        tree[a] = b

for i in range(2,N+1):
    print(tree[i])
