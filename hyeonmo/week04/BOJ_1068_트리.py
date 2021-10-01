# for문으로 돌면서 삭제할 노드들을 탐색하니까 작은 숫자의 노드번호가 삭제될 서브트리의 맨 밑에있을때
# 아직은 인식되지 않아서 삭제하지 않고 넘어가버림
# 높은숫자가 다 -2로 끊겨버려서 리프노드가 되어버려서 cnt가 초과
# DFS 함수로 삭제할 노드를 시작으로 아래로 내려가면서 차례대로 삭제를 해주자


def DFS(v):
    arr[v] = -2         # 호출되면 삭제(-2)
    if v not in arr:    # 호출된 노드번호가 arr에 없다면(끝부분 까지 삭제)
        return

    for i in range(N):  # 배열 전체를 돌면서 삭제할 노드인지 검사
        if arr[i] == v: # 노드가 가지고 있는 부모값이 현재 호출된(삭제해야할) 값이라면
            DFS(i)      # 자식도 호출해서 삭제
    


N = int(input())
arr = list(map(int,input().split()))
delete = int(input())
cnt = 0

DFS(delete) # 지울 노드 먼저 탐색한다.


for i in range(N):
    if arr[i] != -2 and i not in arr:   # 배열의 i번째 노드가 -2가 아니고 i가 arr에 없다면 리프노드이다. 
        cnt += 1

print(cnt)









