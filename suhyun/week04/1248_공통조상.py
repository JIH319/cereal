# 1248. 공통조상
def pre_order(n):
    global cnt
    if n:               # 유효한 정점이면
        pre_order(t_left[n])
        cnt +=1
        pre_order(t_right[n])

T = int(input())
for tc in range(1,T+1):
    V, E, V1, V2 = map(int,input().split())
    edge = list(map(int, input().split()))
    t_left = [0] * (V+1)  # 부모를 인덱스로 자식번호 저장
    t_right = [0] * (V+1)
    p_list = [0] * (V+1)
    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if t_left[p] == 0:  # p 의 왼쪽 자식이 없으면
            t_left[p] = c
        else:               # p의 왼족 자식이 있으면 오른쪽 자식으로 저장
            t_right[p] = c
        p_list[c] = p
    # V1 에 대한 조상 리스트
    V1_list =[p_list[V1]]
    while p_list[V1_list[-1]]:
        V1_list.append(p_list[V1_list[-1]])
    # V 에 대한 조상 리스트
    V2_list = [p_list[V2]]
    while p_list[V2_list[-1]]:
        V2_list.append(p_list[V2_list[-1]])
    # 조상 리스트의 교집합 = 공통 조상
    union_list = list(set(V1_list) & set(V2_list))
    min_u = 0
    min_c = 1000000000
    # 공통 조상을 순회하여 가장 최단 거리 순회를 찾으면 min_u 와 min_c 에 대입한다.
    for u in union_list:
        cnt = 0
        pre_order(u)
        if cnt<min_c:
            min_u = u
            min_c = cnt
    print('#{} {} {}'.format(tc,min_u,min_c))