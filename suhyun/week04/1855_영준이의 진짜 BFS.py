# 1855. 영준이의 진짜 BFS
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
