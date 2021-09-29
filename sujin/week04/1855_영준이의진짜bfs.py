def bfs():
    # 찾을 노드 큐에 담기
    Q = [1]
    for i in range(1,N+1):
        # i를 부모노드로 하는 정점 j 담기 (i의 자식노드)
        for j in range(1, N+1):
            if tree[j] == i:
                Q.append(j)

    result = 0 # 결과 담을 변수
    while len(Q) != 1:
        start = Q.pop(0) # 현재 위치
        end = Q[0]      # 갈 위치
        
        # end에서 출발해서 start까지 최단거리 구하기
        visited = [-1]*(N+1) # 방문 체크 겸 거리 체크
        visited[end] += 1 # 출발점 0
        q = []
        q.append(end)
        while q:
            # 가고자 하는 곳에서 거꾸로 출발노드 찾아올때까지 반복
            current = q.pop(0)
            # current의 부모노드, 아직 방문 안했다면
            if tree[current] and visited[tree[current]] == -1:
                # 가고자 하는 곳이면
                if tree[current] == start:
                    result += visited[current] + 1
                q.append(tree[current])
                visited[tree[current]] = visited[current] + 1

            # current를 부모노드로 하는 노드, 방문 안했다면 
            for i in range(N+1): 
                if tree[i] == current and visited[i] == -1:
                    # 가고자 하는 곳이면
                    if i == start:
                        result += visited[current] + 1
                    q.append(i)
                    visited[i] = visited[current] + 1
    return result
        

for tc in range(1, int(input())+1):
    N = int(input())
    data = list(map(int, input().split()))
    idx = 0
    tree = [0] * (N+1) # 인덱스 : 노드번호, 값 : 갈 수 있는 노드

    for i in range(2,N+1):
        tree[i] = data[idx]
        idx += 1   # 2번노드부터 차례로 부모노드 저장 
    
    # # 찾을 노드 큐에 담기
    # Q = [1]
    # for i in range(1,N+1):
    #     # i를 부모노드로 하는 정점 j 담기 (i의 자식노드)
    #     for j in range(1, N+1):
    #         if tree[j] == i:
    #             Q.append(j)

    # result = 0 # 결과 담을 변수
    # while len(Q) != 1:
    #     start = Q.pop(0) # 현재 위치
    #     end = Q[0]      # 갈 위치
    #     result += bfs(start,end) # 거리구하기
    result = bfs()
    print('#{} {}'.format(tc,result))