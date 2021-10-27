### 1949_등산로조성

```python
#  ① 등산로는 가장 높은 봉우리에서 시작해야 한다.

#  ② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
#        즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.

#  ③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.

# N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다

# 2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)

# 3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)

# 4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.

# 5. 지도에서 가장 높은 봉우리는 최대 5개이다.

# 6. 지형은 정수 단위로만 깎을 수 있다.

# 7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

'''

10        
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2       
1 2 1     
2 1 2
1 2 1

#1 6
#2 3
'''
dir = [(-1,0),(0,1),(1,0),(0,-1)] # 상우하좌 4방향
def dfs(current,c_height,path,construction):
    global result
    # print(current)
    cr,cc = current
    visited[cr][cc] = 1
    for dr,dc in dir:
        nr,nc = cr+dr,cc+dc
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            # 높이가 더 낮은 곳이면,
            if c_height > arr[nr][nc]:
                path.append(arr[nr][nc])
                # print(cr,cc,'에서 ',nr,nc,'로 현재 path는',path,'공사 : ',construction)
                dfs((nr,nc),arr[nr][nc],path,construction)
                path.remove(arr[nr][nc])
            # 높이가 같거나 높은 곳이면
            else:
                # 아직 공사 안했고, 공사를 통해 건너갈 수 있다면 >> 공사 
                if construction == 0 and c_height > arr[nr][nc] - K:
                    path.append(arr[nr][nc]-1)
                    # print(cr,cc,'에서 ',nr,nc,'로 현재 path는',path,'공사 : ',construction)
                    dfs((nr,nc),c_height-1,path,1)
                    # 돌아온 뒤 초기화
                    path.remove(arr[nr][nc]-1)
                # 이미 공사 했다면
                else:
                    if result < len(path):
                        result = len(path)         
                    
    visited[cr][cc] = 0
    


for tc in range(1,int(input())+1):
    # N*N배열, K : 최대 공사 가능 깊이 (1 ≤ K ≤ 5)
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 최대 높이 찾기
    max_h = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_h:
                max_h = arr[i][j]

    result = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 최대 높이 봉우리면
            if arr[i][j] == max_h:
                # print('dfs ',i,j,'에서 시작')
                dfs((i,j),arr[i][j],[arr[i][j]],0)
    print('#{} {}'.format(tc,result))
```







### 2003_bkj_수들의합

```python
# 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수
N,M = map(int,(input().split()))
data = list(map(int,input().split()))

tmp = 0 # M <= tmp 될때까지 누적합 담을 변수
cnt = 0 # tmp == M 가 되면 + 1 : M 이 되는 경우의 수 
sidx = 0 # 탐색 누적합 시작 인덱스
idx = 0 # data 탐색 인덱스

while idx < N:
    tmp += data[idx]
    if tmp >= M:
        # 수열의 합이 M
        if tmp == M:
            cnt += 1          
        # tmp >= M 일때,
        # # 누적합 변수 초기화, 경우의 수 +1, 
        # 누적합 시작인덱스 다음부터 다시 탐색   
        tmp = 0
        sidx = sidx + 1
        idx = sidx
        continue 
    idx += 1 

print(cnt)    

```

