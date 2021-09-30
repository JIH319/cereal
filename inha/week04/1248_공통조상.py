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