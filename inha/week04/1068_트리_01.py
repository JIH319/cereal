import sys
input = sys.stdin.readline


def tree_del(d):
    for i in range(N):
        if p_list[i] == d:
            p_list[i] = -2
            tree_del(i)


def cnt_tn():
    cnt = 0
    for i in range(N):
        if p_list[i] != -2:
            if i not in p_list:
                cnt += 1
    return cnt


N = int(input())
p_list = list(map(int, input().split()))
D = int(input())

p_list[D] = -2
tree_del(D)
print(cnt_tn())