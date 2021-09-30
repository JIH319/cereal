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
