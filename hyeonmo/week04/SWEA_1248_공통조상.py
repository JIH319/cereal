# 1. 주어진 정점 V1,V2의 공통조상에서 제일 가까운 정점을 찾고
# 2. 찾은 정점을 루트로 하는 서브트리의 크기를 구하자.

# 부모자식 순서로 주어지는 간선을 이루는 두 정점을 각 왼쪽과 오른쪽 자식이라는 배열에 넣어준다.
# 왼쪽자식인지 오른쪽 자식인지는 중요하지 않다고 한다.

# 그럼 1. 트리를 만든 후에
# 2. 후위순회로 탐색을 하며 V1과 V2을 우선 찾자!
# 3. 찾고나면 올라 오면서 정점을 임의의 배열에 저장하자
# 4. V2를 따로 찾기 위해서 V1을 찾으면 더 탐색하지 않는 조건을 걸어두자!
# 5. V1과 V2의 조상노드들을 각 다른 배열에 순서대로 넣으면 무엇이 가장 가까운 공통 조상노드인지 알수있다.
# 6. 찾은 공통 조상으로 탐색을 다시 실행하고 탐색하면서 갯수를 세어준다.



def search_V1(v,point):
    global find_V1
    if v == 0:
        return
    if find_V1 == 1:
        return
    
    search_V1(left[v],point)
    search_V1(right[v],point)
    if v == point:
        find_V1 = 1
    if find_V1 == 1:
        V1_p.append(v)

def search_V2(v,point):
    global find_V2
    if v == 0:
        return
    if find_V2 == 1:
        return
    
    search_V2(left[v],point)
    search_V2(right[v],point)
    if v == point:
        find_V2 = 1
    if find_V2 == 1:
        V2_p.append(v)

def search_subtree(v):
    global cnt
    if v == 0:
        return
    search_subtree(left[v])
    search_subtree(right[v])
    cnt += 1


T = int(input())
for tc in range(1,T+1):
    V,E,V1,V2 = map(int,input().split())
    edge = list(map(int,input().split()))
    left = [0]*(V+1)
    right = [0]*(V+1)
    V1_p= []
    V2_p = []
    find_V1 = 0
    find_V2 = 0
    cnt = 0
    key = 0


    for i in range(0,E*2,2):
        if not left[edge[i]]:
            left[edge[i]] = edge[i+1]
        else:
            right[edge[i]] = edge[i+1]
    search_V1(1,V1)
    search_V2(1,V2)

    for j in V1_p:
        if j in V2_p:
            key = j
            break

    search_subtree(key)

    print(f'#{tc} {key} {cnt}')
