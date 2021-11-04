

# 수들의 합2

```python
"""
4 2
1 1 1 1

10 5
1 2 3 4 2 5 3 1 1 2
"""

N, M = map(int,input().split())
data = list(map(int,input().split()))
cnt = 0

for i in range(N):
    tmp_sum = 0
    for j in range(i, N):
        tmp_sum += data[j]
        if tmp_sum == M: # 하나의 원소가 바로 그 M의 값이 되면 바로 끝
            cnt += 1
            break
        elif tmp_sum > M: # 더해주다가 그 값이 M을 넘게되면 끝
            break
print(cnt)


```



# 등산로 조성

```python
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def dfs(r, c, height, length, work):  # 현재 높이. 등산로 길이, 공사했나안했나 쳌

    global result

    if length > result: # 길이 최대값 저장
        result = length

    visited[r][c] = 1 # 현재 위치 방문쳌

    for i in range(4): #4방향 탐색
        nr = r + dr[i]
        nc = c + dc[i]

        #요 애들은 지나가자~~
        if 0 > nr or nr >= N or 0 > nc or nc >= N or visited[nr][nc]: continue

        # 다음 갈 데이터가 현재 가지고있는 높이보다 더 낮다면
        if data[nr][nc] < height:
            dfs(nr, nc, data[nr][nc], length + 1, work) 
            #길이 1늘어나고 좌표바뀌고 진행

        # 아직 공사안했고 다음 갈 데이터에서 공사해서 줄일수있는 
        #그 값이 현재 데이터보다 작다면
        elif work and height > data[nr][nc] - K:
            # 좌표이동하고 이동했으니까 1칸 작고, 길이 1늘어나고, 공사했다 첵
            dfs(nr, nc, data[r][c] - 1,  length + 1, 0)

    #다시 풀어준다
    visited[r][c] = 0


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())

    data = []
    max_h = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        max_h = max(max_h, max(tmp))
        data.append(tmp)

    visited = [[0] * N for _ in range(N)]
    # print(max_h)
    result = 0
    for r in range(N):
        for c in range(N):
            if data[r][c] == max_h: #최고 길이 찾으면 바로고고
                dfs(r, c, max_h, 1, 1) # 좌표,현재 높이 ,길이, 공사유무

    print('#{} {}'.format(tc, result))

```

# 도로 네트워크

```python
# 아니 이거 예제 이해는 가는데 우에 할지 모르겠다....
# 그 공통조상 LCA 인데... 서로 그 위치라고 해야하나 높이가 다르면 같을때 까지 올라가고 올라가면서도 도로의 길이는 다 넣어주고
# 공통조상 찾을때까지 같이 올라가는데 유튭 LCA 영상에서 하나씩 올라가는거 보다 2의 제곱만큼 올라가는게 빠르다고 하던데...
# 그래서 찾으면서 도로의 길이를 다 저장해주면 그 값중 최소 최대값을 구하는건데 우째 건들지...
```



# 
