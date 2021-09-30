# 1068. 트리
# 리프노드를 구하자!
def dfs(e, p):
    p[e] = -10
    for i in range(len(p)):
        if e == p[i]:
            dfs(i, p)


# 노드의 개수 N
N = int(input())
# 노드의 부모 p_list
p_list = list(map(int, input().split()))
# 지울 노드 eraser_node 줄여서 en
en = int(input())
dfs(en, p_list)
cnt = 0
print(p_list)
for i in range(len(p_list)):
    # p_list[i] != -10 : 삭제하여 없어진 노드들을 뜻함.
    # i in p_list: i번째 번호가 p_list 에 있다 = 리프노드가 아니다 란 뜻.
    # 즉, 반대로 생각하여 i번째 번호가 p_list 에도 없다면 리프노드란 뜻이다.
    if p_list[i] != -10 and i not in p_list:
        cnt += 1
print(cnt)
