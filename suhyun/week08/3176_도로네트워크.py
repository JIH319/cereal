# 3176. 도로 네트워크
from collections import deque


def solve(s, e):
    que = deque()
    que.append((s, 0xffffff, -1))
    while que:
        cc, min_road, max_road = que.popleft()
        if cc == e:
            return min_road, max_road
        for i in range(1, N + 1):
            if adj[cc][i]:
                min_tmp = min(min_road, adj[cc][i])
                max_tmp = max(max_road, adj[cc][i])
                que.append((i, min_tmp, max_tmp))


N = int(input())  # 첫째 줄에 N이 주어진다.(2<=N<=100,000)
adj = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(N - 1):
    s, e, w = map(int, input().split())
    adj[s][e] = w
    adj[e][s] = w
K = int(input())  # 서로다른 자연수 D , E 의 숫자
for _ in range(K):
    start, end = map(int, input().split())
    min_result, max_result = solve(start, end)
    print(min_result, max_result)
